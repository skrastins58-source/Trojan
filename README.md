# Trojan

A simple Python application.

## Requirements

- Python 3.6 or higher

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/skrastins58-source/Trojan.git
   cd Trojan
   ```

2. Install dependencies (optional, no external dependencies required):
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Building the Project

No build step is required for this Python application.

### Running the Application

Run the application using Python:

```bash
python trojan.py
```

Or make it executable and run directly:

```bash
chmod +x trojan.py
./trojan.py
```

The application will start and display status messages. Press `Ctrl+C` to exit gracefully.

## Features

- Graceful startup and shutdown
- Proper error handling and logging
- Signal handling for clean termination

## Troubleshooting

If the application fails to start:

1. Ensure you have Python 3.6 or higher installed:
   ```bash
   python --version
   ```

2. Check the console output for any error messages
3. Verify file permissions are correct