# Trojan

A robust Python application demonstrating best practices for error handling, logging, and graceful shutdown procedures.

## Overview

This application serves as a minimal but complete example of a well-structured Python application featuring:

- **Multi-level logging** (DEBUG, INFO, WARNING, ERROR) with comprehensive output
- **Graceful signal handling** for clean shutdown procedures (SIGINT, SIGTERM)
- **User-friendly error messages** with helpful troubleshooting hints
- **Command-line interface** with help and version options
- **System requirements validation** with clear error reporting
- **Configuration stub** for future extensibility
- **Comprehensive test suite** for verification

## Requirements

- **Python 3.6 or higher** (Python 3.8+ recommended)
- **Write permissions** in the execution directory (for optimal functionality)
- **Virtual environment** (strongly recommended)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/skrastins58-source/Trojan.git
cd Trojan
```

### 2. Set Up Virtual Environment (Recommended)

Creating a virtual environment ensures clean dependency management:

```bash
# Create virtual environment
python -m venv trojan_env

# Activate virtual environment
# On Linux/macOS:
source trojan_env/bin/activate
# On Windows:
trojan_env\Scripts\activate

# Install dependencies (optional - no external dependencies required)
pip install -r requirements.txt
```

### 3. Verify Installation

```bash
python trojan.py --version
```

Expected output:
```
Trojan 1.0.0
```

## Usage

### Basic Usage

Run the application with default settings:

```bash
python trojan.py
```

**Successful startup example:**
```
2025-09-13 03:29:20,312 - INFO - Starting Trojan v1.0.0
2025-09-13 03:29:20,313 - INFO - Trojan application startup completed successfully
2025-09-13 03:29:20,313 - INFO - Application is now running - Press Ctrl+C to exit gracefully
2025-09-13 03:29:30,313 - INFO - Application running normally (uptime: 60 seconds)
```

### Command Line Options

#### Show Help Information
```bash
python trojan.py --help
```

#### Show Version
```bash
python trojan.py --version
```

#### Set Logging Level
```bash
# Debug level (most verbose)
python trojan.py --log-level DEBUG

# Info level (default)
python trojan.py --log-level INFO

# Warning level
python trojan.py --log-level WARNING

# Error level (least verbose)
python trojan.py --log-level ERROR
```

**Debug logging example:**
```
2025-09-13 03:29:20,312 - DEBUG - Logging initialized at DEBUG level
2025-09-13 03:29:20,312 - INFO - Starting Trojan v1.0.0
2025-09-13 03:29:20,313 - DEBUG - Command line arguments: {'log_level': 'DEBUG'}
2025-09-13 03:29:20,313 - DEBUG - Python version check passed: 3.12.3
2025-09-13 03:29:20,313 - DEBUG - Write permissions check passed
2025-09-13 03:29:20,313 - DEBUG - Setting up signal handlers...
2025-09-13 03:29:20,313 - DEBUG - Signal handlers configured successfully
```

### Make Executable (Optional)

For direct execution without specifying python:

```bash
chmod +x trojan.py
./trojan.py
```

### Graceful Shutdown

The application responds to standard shutdown signals:

- **Ctrl+C (SIGINT)** - Interactive shutdown
- **SIGTERM** - System shutdown signal

**Shutdown example:**
```
2025-09-13 03:29:37,208 - INFO - Received SIGTERM signal, initiating graceful shutdown...
2025-09-13 03:29:37,209 - INFO - Starting cleanup procedures...
2025-09-13 03:29:37,309 - INFO - Cleanup completed successfully
2025-09-13 03:29:37,309 - INFO - Trojan application shutdown complete
```

## Testing

Run the comprehensive test suite to verify functionality:

```bash
python test_trojan.py
```

**Test output example:**
```
==================================================
Running Trojan Application Tests
==================================================
Testing --help flag...
✅ Help flag test passed

Testing --version flag...
✅ Version flag test passed

Testing application startup and logging...
✅ Startup and logging test passed

Testing debug level logging...
✅ Debug logging test passed

Testing invalid argument handling...
✅ Invalid argument handling test passed

==================================================
Test Results: 5/5 tests passed
🎉 All tests passed!
```

## Features

### Robust Error Handling
- **System requirements validation** with helpful error messages
- **Permission checking** with appropriate warnings
- **Python version verification** with upgrade suggestions
- **Graceful degradation** for non-critical errors

### Comprehensive Logging
- **Multiple log levels** for different use cases
- **Structured log format** with timestamps and levels
- **Debug information** for troubleshooting
- **Status updates** during normal operation

### Signal Handling
- **SIGINT (Ctrl+C)** handling for interactive shutdown
- **SIGTERM** handling for system shutdown
- **Cleanup procedures** before exit
- **Resource management** and state saving

### Command Line Interface
- **Help system** with usage examples
- **Version information** display
- **Configurable logging levels**
- **Input validation** with clear error messages

## Troubleshooting

### Common Issues and Solutions

#### 1. Python Version Error

**Error:**
```
ERROR: Python 3.6 or higher is required. You have 2.7.x
HINT: Update Python or use a virtual environment with a newer version.
```

**Solutions:**
- Install Python 3.6 or higher from [python.org](https://python.org)
- Use a virtual environment with a newer Python version
- On Ubuntu/Debian: `sudo apt install python3.8`
- On CentOS/RHEL: `sudo yum install python38`
- On macOS with Homebrew: `brew install python@3.8`

#### 2. Permission Errors

**Error:**
```
WARNING - Limited write permissions in current directory: [Errno 13] Permission denied
HINT: Run from a directory where you have write permissions
```

**Solutions:**
- Change to a directory where you have write permissions: `cd ~/`
- Create a dedicated directory: `mkdir ~/trojan_workspace && cd ~/trojan_workspace`
- Check current permissions: `ls -la`

#### 3. Module Import Errors

**Error:**
```
Fatal error during application execution: No module named 'module_name'
HINT: Check Python installation and ensure all required modules are available
```

**Solutions:**
- Verify Python installation: `python --version`
- Check if running in correct virtual environment
- Reinstall Python if necessary
- This application uses only standard library - no external modules required

#### 4. Application Won't Start

**General troubleshooting steps:**

1. **Check Python version:**
   ```bash
   python --version
   # Should be 3.6 or higher
   ```

2. **Verify file permissions:**
   ```bash
   ls -la trojan.py
   # Should show read permissions
   ```

3. **Test with verbose logging:**
   ```bash
   python trojan.py --log-level DEBUG
   ```

4. **Check for error details:**
   ```bash
   python trojan.py 2>&1 | tee debug.log
   ```

#### 5. Virtual Environment Issues

**Setting up virtual environment:**
```bash
# Remove existing environment if corrupted
rm -rf trojan_env

# Create new environment
python3 -m venv trojan_env

# Activate environment
source trojan_env/bin/activate  # Linux/macOS
# OR
trojan_env\Scripts\activate  # Windows

# Verify environment
which python
python --version
```

### Getting Help

If you encounter issues not covered above:

1. **Enable debug logging:** `python trojan.py --log-level DEBUG`
2. **Check the error messages** for specific hints
3. **Verify system requirements** are met
4. **Test with the included test suite:** `python test_trojan.py`

### System Requirements Verification

Run this command to verify your system meets all requirements:

```bash
python -c "
import sys
print(f'Python version: {sys.version}')
print(f'Version info: {sys.version_info}')
print(f'Meets requirements: {sys.version_info >= (3, 6)}')
"
```

## Development

### Project Structure
```
Trojan/
├── trojan.py           # Main application
├── test_trojan.py      # Test suite
├── requirements.txt    # Dependencies and documentation
└── README.md          # This file
```

### Extension Points

The application is designed for easy extension:

- **Configuration system** - Extend the `CONFIG` dictionary
- **Logging destinations** - Add file or network handlers
- **Command line options** - Extend the argument parser
- **Cleanup procedures** - Add custom cleanup in `cleanup_and_exit()`
- **Application logic** - Replace the main loop with actual work

For development, consider adding these optional tools to requirements.txt:
```
pytest>=6.0.0      # Advanced testing
black>=21.0.0       # Code formatting  
flake8>=3.8.0       # Code linting
mypy>=0.800         # Type checking
```