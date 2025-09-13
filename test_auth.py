#!/usr/bin/env python3
"""
Test script for Trojan Authentication System
Tests the core authentication functionality.
"""

import sqlite3
import hashlib
import sys
import os

def test_database_structure():
    """Test that the database has the correct structure"""
    print("🔍 Testing database structure...")
    
    db_path = 'instance/trojan.db'
    if not os.path.exists(db_path):
        print("❌ Database file not found!")
        return False
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Check if user table exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='user';")
    result = cursor.fetchone()
    
    if not result:
        print("❌ User table not found!")
        return False
    
    # Check table structure
    cursor.execute("PRAGMA table_info(user);")
    columns = cursor.fetchall()
    
    expected_columns = {'id', 'email', 'password_hash'}
    actual_columns = {col[1] for col in columns}
    
    if not expected_columns.issubset(actual_columns):
        print(f"❌ Missing columns. Expected: {expected_columns}, Found: {actual_columns}")
        return False
    
    conn.close()
    print("✅ Database structure is correct!")
    return True

def test_password_hashing():
    """Test password hashing functionality"""
    print("🔍 Testing password hashing...")
    
    # Import our app modules
    sys.path.append('.')
    from app import app, db, User
    
    with app.app_context():
        # Create a test user
        test_email = "test@example.com"
        test_password = "testpassword123"
        
        # Delete any existing test user
        existing_user = User.query.filter_by(email=test_email).first()
        if existing_user:
            db.session.delete(existing_user)
            db.session.commit()
        
        # Create new user
        user = User(email=test_email)
        user.set_password(test_password)
        
        # Test that password is hashed (not stored in plain text)
        if user.password_hash == test_password:
            print("❌ Password is not hashed!")
            return False
        
        # Test that password verification works
        if not user.check_password(test_password):
            print("❌ Password verification failed!")
            return False
        
        # Test that wrong password fails
        if user.check_password("wrongpassword"):
            print("❌ Wrong password verification should fail!")
            return False
        
        # Save to database
        db.session.add(user)
        db.session.commit()
        
        # Verify user was saved
        saved_user = User.query.filter_by(email=test_email).first()
        if not saved_user:
            print("❌ User was not saved to database!")
            return False
        
        if not saved_user.check_password(test_password):
            print("❌ Saved user password verification failed!")
            return False
        
        # Clean up
        db.session.delete(saved_user)
        db.session.commit()
    
    print("✅ Password hashing works correctly!")
    return True

def test_email_validation():
    """Test email validation"""
    print("🔍 Testing email validation...")
    
    sys.path.append('.')
    from app import is_valid_email
    
    valid_emails = [
        "test@example.com",
        "user.name@domain.co.uk",
        "test123@test-domain.org"
    ]
    
    invalid_emails = [
        "invalid-email",
        "@domain.com",
        "user@",
        "user name@domain.com",
        ""
    ]
    
    for email in valid_emails:
        if not is_valid_email(email):
            print(f"❌ Valid email '{email}' was rejected!")
            return False
    
    for email in invalid_emails:
        if is_valid_email(email):
            print(f"❌ Invalid email '{email}' was accepted!")
            return False
    
    print("✅ Email validation works correctly!")
    return True

def run_all_tests():
    """Run all tests"""
    print("🛡️ Running Trojan Authentication System Tests\n")
    
    tests = [
        test_database_structure,
        test_email_validation,
        test_password_hashing
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        try:
            if test():
                passed += 1
        except Exception as e:
            print(f"❌ Test failed with error: {e}")
        print()
    
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Authentication system is working correctly.")
        return True
    else:
        print("⚠️ Some tests failed. Please check the implementation.")
        return False

if __name__ == "__main__":
    os.chdir('/home/runner/work/Trojan/Trojan')
    success = run_all_tests()
    sys.exit(0 if success else 1)