
class handleBaseClass:
    """Extend this class to implement custom extract handlers"""
    
    def __init__(self,config):
        self.config = config

        # Store hash of the original file so we don't delete the wrong things
        with open(config['fileName'],"rb") as f:
            self.sha256 = hashlib.sha256(f.read()).digest()

    def extract(self):
        config = self.config

        # Do we need to remove the file?
        if config['rm']:

            # Does it still exist and has it not changed?
            if os.path.exists(config['fileName']) and self._hashNotChanged():
                logger.debug("Removing original file")
                os.remove(config['fileName']) 

            
    def _hashNotChanged(self):
        """Make sure the file hash hasn't changed""" 
    
        with open(self.config['fileName'],"rb") as f:
            return self.sha256 == hashlib.sha256(f.read()).digest()

import logging
import hashlib
import os

logger = logging.getLogger("extract.handlers")
