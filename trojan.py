#!/usr/bin/env python3
"""
Trojan - A simple application
"""

import sys
import logging
import signal


def setup_logging():
    """Set up basic logging configuration."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )


def signal_handler(signum, frame):
    """Handle shutdown signals gracefully."""
    logging.info(f"Received signal {signum}, shutting down gracefully...")
    sys.exit(0)


def main():
    """Main application entry point."""
    try:
        # Set up logging
        setup_logging()
        
        # Set up signal handlers for graceful shutdown
        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGTERM, signal_handler)
        
        logging.info("Trojan application starting...")
        
        # Application logic would go here
        logging.info("Trojan application is running successfully!")
        logging.info("Press Ctrl+C to exit.")
        
        # Keep the application running
        try:
            while True:
                pass
        except KeyboardInterrupt:
            logging.info("Keyboard interrupt received, shutting down...")
            
    except Exception as e:
        logging.error(f"Fatal error during startup: {e}", exc_info=True)
        sys.exit(1)
    
    logging.info("Trojan application shut down complete.")


if __name__ == "__main__":
    main()