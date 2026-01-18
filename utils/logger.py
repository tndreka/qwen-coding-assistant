"""Logging configuration."""
import logging
import colorlog
from core.config import Config

def setup_logger(name:  str = __name__):
    """Setup colored console logger."""
    logger = logging.getLogger(name)
    logger.setLevel(Config.LOG_LEVEL)
    
    if logger.handlers:
        return logger
    
    handler = colorlog.StreamHandler()
    handler.setFormatter(colorlog.ColoredFormatter(
        '%(log_color)s%(levelname)-8s%(reset)s %(message)s',
        log_colors={
            'DEBUG': 'cyan',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL':  'red,bg_white',
        }
    ))
    
    logger.addHandler(handler)
    return logger