#!/usr/bin/env python3
"""
Test script for Trojan application

This script tests:
- Application startup and shutdown
- CLI argument parsing
- Logging output verification
- Signal handling
- Error conditions
"""

import subprocess
import sys
import time
import os
import signal
import tempfile


def run_command(cmd, timeout=10):
    """
    Run a command and return the result.
    
    Args:
        cmd (list): Command to run as list of strings
        timeout (int): Maximum time to wait for command
        
    Returns:
        tuple: (returncode, stdout, stderr)
    """
    try:
        result = subprocess.run(
            cmd, 
            capture_output=True, 
            text=True, 
            timeout=timeout
        )
        return result.returncode, result.stdout, result.stderr
    except subprocess.TimeoutExpired:
        return -1, "", "Command timed out"


def test_help_flag():
    """Test --help flag functionality."""
    print("Testing --help flag...")
    returncode, stdout, stderr = run_command(['python', 'trojan.py', '--help'])
    
    if returncode != 0:
        print(f"❌ Help flag test failed: {stderr}")
        return False
    
    if 'Trojan - A simple Python application' not in stdout:
        print("❌ Help output doesn't contain expected description")
        return False
    
    if '--version' not in stdout or '--log-level' not in stdout:
        print("❌ Help output missing expected options")
        return False
    
    print("✅ Help flag test passed")
    return True


def test_version_flag():
    """Test --version flag functionality."""
    print("Testing --version flag...")
    returncode, stdout, stderr = run_command(['python', 'trojan.py', '--version'])
    
    if returncode != 0:
        print(f"❌ Version flag test failed: {stderr}")
        return False
    
    if 'Trojan 1.0.0' not in stdout:
        print(f"❌ Version output incorrect. Got: {stdout.strip()}")
        return False
    
    print("✅ Version flag test passed")
    return True


def test_startup_and_logging():
    """Test application startup and logging output."""
    print("Testing application startup and logging...")
    
    # Start the application with INFO logging
    process = subprocess.Popen(
        ['python', 'trojan.py', '--log-level', 'INFO'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    # Let it run for a few seconds
    time.sleep(3)
    
    # Send SIGTERM for graceful shutdown
    process.send_signal(signal.SIGTERM)
    
    # Wait for shutdown
    try:
        stdout, stderr = process.communicate(timeout=10)
    except subprocess.TimeoutExpired:
        process.kill()
        print("❌ Application didn't shut down gracefully within timeout")
        return False
    
    # Check exit code
    if process.returncode != 0:
        print(f"❌ Application exited with non-zero code: {process.returncode}")
        print(f"STDERR: {stderr}")
        return False
    
    # Verify expected log messages
    expected_messages = [
        "Starting Trojan v1.0.0",
        "Trojan application startup completed successfully",
        "Received SIGTERM signal",
        "Starting cleanup procedures",
        "Cleanup completed successfully",
        "Trojan application shutdown complete"
    ]
    
    for message in expected_messages:
        if message not in stdout:
            print(f"❌ Expected log message not found: {message}")
            print(f"Actual output: {stdout}")
            return False
    
    print("✅ Startup and logging test passed")
    return True


def test_debug_logging():
    """Test debug level logging."""
    print("Testing debug level logging...")
    
    # Start with DEBUG logging
    process = subprocess.Popen(
        ['python', 'trojan.py', '--log-level', 'DEBUG'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    # Let it run briefly
    time.sleep(2)
    
    # Terminate gracefully
    process.send_signal(signal.SIGTERM)
    
    try:
        stdout, stderr = process.communicate(timeout=10)
    except subprocess.TimeoutExpired:
        process.kill()
        print("❌ Debug logging test timed out")
        return False
    
    # Check for debug messages
    debug_messages = [
        "Logging initialized at DEBUG level",
        "Command line arguments:",
        "Python version check passed:",
        "Setting up signal handlers...",
        "Signal handlers configured successfully"
    ]
    
    for message in debug_messages:
        if message not in stdout:
            print(f"❌ Expected debug message not found: {message}")
            return False
    
    print("✅ Debug logging test passed")
    return True


def test_invalid_arguments():
    """Test handling of invalid command line arguments."""
    print("Testing invalid argument handling...")
    
    # Test invalid log level
    returncode, stdout, stderr = run_command(['python', 'trojan.py', '--log-level', 'INVALID'])
    
    if returncode == 0:
        print("❌ Application should have failed with invalid log level")
        return False
    
    if 'invalid choice' not in stderr.lower():
        print(f"❌ Expected error message about invalid choice not found in: {stderr}")
        return False
    
    print("✅ Invalid argument handling test passed")
    return True


def main():
    """Run all tests."""
    print("=" * 50)
    print("Running Trojan Application Tests")
    print("=" * 50)
    
    # Change to the script directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    tests = [
        test_help_flag,
        test_version_flag,
        test_startup_and_logging,
        test_debug_logging,
        test_invalid_arguments
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        try:
            if test():
                passed += 1
            print()  # Add spacing between tests
        except Exception as e:
            print(f"❌ Test {test.__name__} failed with exception: {e}")
            print()
    
    print("=" * 50)
    print(f"Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed!")
        return 0
    else:
        print("❌ Some tests failed")
        return 1


if __name__ == "__main__":
    sys.exit(main())