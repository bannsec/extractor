import logging

logger = logging.getLogger("extract.handlers")

class handleBaseClass:
    """Extend this class to implement custom extract handlers"""
    
    def __init__(self,config):
        self.config = config

    def extract(self):
        logger.warn("Extract isn't implemented.")
    
