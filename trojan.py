#!/usr/bin/env python3
"""
Trojan - A simple Python application with robust logging and error handling

This application provides a minimal but complete example of:
- Multi-level logging (DEBUG, INFO, WARNING, ERROR)
- Graceful signal handling and shutdown procedures  
- User-friendly error messages and troubleshooting hints
- Command-line interface with help and version options
- Configuration stub for future extensibility
"""

import sys
import logging
import signal
import argparse
import os
import time

# Application version
__version__ = "1.0.0"

# Global configuration placeholder - can be extended for config files or environment variables
CONFIG = {
    'log_level': 'INFO',
    'shutdown_timeout': 5,
    'app_name': 'Trojan'
}


def setup_logging(log_level=None):
    """
    Set up comprehensive logging configuration with multiple levels.
    
    Args:
        log_level (str): Logging level (DEBUG, INFO, WARNING, ERROR)
    """
    if log_level is None:
        log_level = CONFIG.get('log_level', 'INFO')
    
    # Convert string level to logging constant
    numeric_level = getattr(logging, log_level.upper(), logging.INFO)
    
    logging.basicConfig(
        level=numeric_level,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )
    
    # Log the logging setup completion
    logging.debug(f"Logging initialized at {log_level} level")


def check_system_requirements():
    """
    Check system requirements and provide helpful error messages.
    
    Returns:
        bool: True if requirements are met, False otherwise
    """
    # Check Python version
    if sys.version_info < (3, 6):
        print(f"ERROR: Python 3.6 or higher is required. You have {sys.version}", file=sys.stderr)
        print("HINT: Update Python or use a virtual environment with a newer version.", file=sys.stderr)
        return False
    
    logging.debug(f"Python version check passed: {sys.version}")
    
    # Check if we can write to current directory (for future log files, etc.)
    try:
        test_file = '.trojan_write_test'
        with open(test_file, 'w') as f:
            f.write('test')
        os.remove(test_file)
        logging.debug("Write permissions check passed")
    except (PermissionError, OSError) as e:
        logging.warning(f"Limited write permissions in current directory: {e}")
        logging.warning("HINT: Run from a directory where you have write permissions")
        # Don't fail on this - just warn
    
    return True


def signal_handler(signum, frame):
    """
    Handle shutdown signals gracefully with comprehensive cleanup.
    
    Args:
        signum (int): Signal number received
        frame: Current stack frame (unused)
    """
    signal_names = {signal.SIGINT: 'SIGINT', signal.SIGTERM: 'SIGTERM'}
    signal_name = signal_names.get(signum, f'Signal {signum}')
    
    logging.info(f"Received {signal_name} signal, initiating graceful shutdown...")
    
    # Perform cleanup operations
    cleanup_and_exit()


def cleanup_and_exit(exit_code=0):
    """
    Perform all necessary cleanup operations before exit.
    
    Args:
        exit_code (int): Exit code to use when terminating
    """
    logging.info("Starting cleanup procedures...")
    
    # Add any cleanup logic here (closing files, network connections, etc.)
    # For now, just log the cleanup steps
    logging.debug("Cleaning up resources...")
    logging.debug("Closing any open connections...")
    logging.debug("Saving state if necessary...")
    
    # Simulate brief cleanup time
    time.sleep(0.1)
    
    logging.info("Cleanup completed successfully")
    logging.info(f"{CONFIG['app_name']} application shutdown complete")
    sys.exit(exit_code)


def parse_arguments():
    """
    Parse command line arguments.
    
    Returns:
        argparse.Namespace: Parsed arguments
    """
    parser = argparse.ArgumentParser(
        description='Trojan - A simple Python application with robust error handling',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                    # Run with default settings
  %(prog)s --version          # Show version information
  %(prog)s --help             # Show this help message

For troubleshooting, ensure you have Python 3.6+ and appropriate permissions.
        """
    )
    
    parser.add_argument(
        '--version', 
        action='version', 
        version=f'{CONFIG["app_name"]} {__version__}'
    )
    
    parser.add_argument(
        '--log-level',
        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR'],
        default='INFO',
        help='Set logging level (default: INFO)'
    )
    
    return parser.parse_args()


def main():
    """
    Main application entry point with comprehensive error handling.
    
    This function handles:
    - Command line argument parsing
    - System requirements validation
    - Logging configuration
    - Signal handler setup
    - Application lifecycle management
    """
    try:
        # Parse command line arguments first (for --help, --version, etc.)
        args = parse_arguments()
        
        # Set up logging with specified level
        setup_logging(args.log_level)
        
        logging.info(f"Starting {CONFIG['app_name']} v{__version__}")
        logging.debug(f"Command line arguments: {vars(args)}")
        
        # Check system requirements and provide helpful error messages
        if not check_system_requirements():
            logging.error("System requirements not met - exiting")
            sys.exit(1)
        
        # Set up signal handlers for graceful shutdown
        logging.debug("Setting up signal handlers...")
        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGTERM, signal_handler)
        logging.debug("Signal handlers configured successfully")
        
        logging.info(f"{CONFIG['app_name']} application startup completed successfully")
        logging.info("Application is now running - Press Ctrl+C to exit gracefully")
        
        # Main application loop - this is where actual work would be done
        logging.debug("Entering main application loop...")
        try:
            loop_count = 0
            while True:
                # Simulate some work and periodic status logging
                time.sleep(10)  # Check every 10 seconds
                loop_count += 1
                
                if loop_count % 6 == 0:  # Log status every minute
                    logging.info(f"Application running normally (uptime: {loop_count * 10} seconds)")
                
        except KeyboardInterrupt:
            # This should be caught by signal handler, but just in case
            logging.info("Keyboard interrupt received in main loop")
            cleanup_and_exit(0)
            
    except SystemExit:
        # Re-raise SystemExit to preserve exit codes
        raise
        
    except Exception as e:
        # Catch any unexpected errors and provide helpful debugging information
        logging.error(f"Fatal error during application execution: {e}", exc_info=True)
        
        # Provide helpful hints based on common error patterns
        error_str = str(e).lower()
        if 'permission' in error_str:
            logging.error("HINT: Check file permissions and try running from a different directory")
        elif 'import' in error_str or 'module' in error_str:
            logging.error("HINT: Check Python installation and ensure all required modules are available")
        elif 'address' in error_str or 'port' in error_str:
            logging.error("HINT: Check network connectivity and ensure required ports are available")
        else:
            logging.error("HINT: Check the error details above and ensure system requirements are met")
        
        # Clean exit even on errors
        cleanup_and_exit(1)


if __name__ == "__main__":
    main()