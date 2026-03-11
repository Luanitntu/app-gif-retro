# Logging module
import os
import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime

class LoggerSetup:
    """Centralized logging configuration"""
    
    _instance = None
    _logger = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(LoggerSetup, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        if self._initialized:
            return
        
        self._initialized = True
        self.logs_dir = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            'logs'
        )
        self._setup_logger()
    
    def _setup_logger(self):
        """Setup logger with file and console handlers"""
        # Ensure logs directory exists
        os.makedirs(self.logs_dir, exist_ok=True)
        
        # Create logger
        self._logger = logging.getLogger('GifViewer')
        self._logger.setLevel(logging.DEBUG)
        
        # Clear existing handlers
        self._logger.handlers.clear()
        
        # File handler - rotating log file
        log_file = os.path.join(self.logs_dir, 'app.log')
        file_handler = RotatingFileHandler(
            log_file,
            maxBytes=5*1024*1024,  # 5MB
            backupCount=5
        )
        file_handler.setLevel(logging.DEBUG)
        
        # Error log file
        error_log_file = os.path.join(self.logs_dir, 'error.log')
        error_handler = RotatingFileHandler(
            error_log_file,
            maxBytes=5*1024*1024,
            backupCount=5
        )
        error_handler.setLevel(logging.ERROR)
        
        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        
        # Formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        
        file_handler.setFormatter(formatter)
        error_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        
        # Add handlers
        self._logger.addHandler(file_handler)
        self._logger.addHandler(error_handler)
        self._logger.addHandler(console_handler)
        
        # Log startup
        self._logger.info("=" * 60)
        self._logger.info(f"GIF Viewer Started - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        self._logger.info("=" * 60)
    
    @staticmethod
    def get_logger():
        """Get logger instance"""
        instance = LoggerSetup()
        return instance._logger

# Convenience function
def get_logger():
    """Get the global logger"""
    return LoggerSetup.get_logger()
