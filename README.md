# 🛡️ Trojan Authentication System

A secure Flask-based user authentication system with registration, login, and logout functionality.

## Features

- ✅ **User Registration**: Email and password-based registration with validation
- ✅ **Secure Password Storage**: Passwords are hashed using Werkzeug's security functions
- ✅ **Session Management**: Server-side session management for user authentication
- ✅ **Login/Logout**: Complete authentication flow with proper session handling
- ✅ **Input Validation**: Email format validation and password requirements
- ✅ **Error Handling**: User-friendly error messages and flash notifications
- ✅ **Responsive UI**: Clean, modern web interface

## Getting Started

### Prerequisites

- Python 3.7+
- pip (Python package installer)

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Trojan
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

4. Open your browser and navigate to `http://127.0.0.1:5000`

### Usage

1. **Register**: Create a new account with email and password
2. **Login**: Sign in with your credentials
3. **Dashboard**: View your user information when logged in
4. **Logout**: Securely log out of your session

## Security Features

- **Password Hashing**: Uses Werkzeug's `generate_password_hash()` with secure defaults
- **Session Management**: Flask's built-in session management with secure secret key
- **Input Validation**: Server-side validation for email format and password requirements
- **SQL Injection Protection**: Uses SQLAlchemy ORM for database operations

## Project Structure

```
Trojan/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── test_auth.py       # Authentication test suite
├── instance/
│   └── trojan.db      # SQLite database (created automatically)
└── templates/         # HTML templates
    ├── base.html      # Base template
    ├── index.html     # Home page
    ├── register.html  # Registration form
    ├── login.html     # Login form
    └── dashboard.html # User dashboard
```

## Testing

Run the test suite to verify authentication functionality:

```bash
python test_auth.py
```

## Development

The application uses:
- **Flask**: Web framework
- **Flask-SQLAlchemy**: Database ORM
- **Werkzeug**: Password hashing and security utilities
- **SQLite**: Lightweight database (no setup required)

## Security Notes

⚠️ **Important for Production Use:**

1. Change the `SECRET_KEY` in `app.py` to a secure, random value
2. Use a production WSGI server (not Flask's development server)
3. Consider using PostgreSQL or MySQL instead of SQLite for production
4. Implement HTTPS/SSL encryption
5. Add rate limiting for login attempts
6. Consider implementing password strength requirements
7. Add email verification for registration

## License

This project is open source and available under the [MIT License](LICENSE).