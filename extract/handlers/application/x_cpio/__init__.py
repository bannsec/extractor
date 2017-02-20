from extract.handlers import handleBaseClass

class handle(handleBaseClass):

    def extract(self):
        config = self.config

        # Find the base directory of the file
        directory = os.path.dirname(os.path.abspath(config['fileName']))

        # Default to extracting to the same directory
        os.chdir(directory)
        
        # Do the actual extraction
        with open(config['fileName'],"rb") as f:                                            
            for entry in libarchive.public.memory_pour(f.read()):
                pass

        # Call parent handler
        handleBaseClass.extract(self)
        

import logging
import os
import libarchive.public

logger = logging.getLogger('extract.handlers.application.x_cpio')
