import logging
import sys
import os

# Ensure the logs directory exists
os.makedirs("logs", exist_ok=True)

def setup_logger(name: str) -> logging.Logger:
    """
    Sets up a logger for the given agent or module.
    Outputs to both the console and logs/execution.log.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    # Prevent duplicate logs if already configured
    if logger.hasHandlers():
        return logger

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # Console Handler
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.INFO)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    # File Handler
    fh = logging.FileHandler("logs/execution.log")
    fh.setLevel(logging.INFO)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    return logger
