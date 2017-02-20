from extract.handlers import handleBaseClass

class handle(handleBaseClass):

    def extract(self):
        config = self.config

        # Open it up
        b = bz2.BZ2File(config['fileName'])

        # Find the base directory of the file
        directory = os.path.dirname(os.path.abspath(config['fileName']))

        # Determine output file name
        if config['fileName'].endswith(".bz2"):
            outFile = config['fileName'][:-4]
        else:
            outFile = config['fileName'] + "_extracted"
        
        # Do the actual extraction
        # TODO: Maybe we wanna buffer this...
        with open(outFile,"wb") as f:
            f.write(b.read())

        # Call parent handler
        handleBaseClass.extract(self)
        

import bz2        
import logging
import os

logger = logging.getLogger('extract.handlers.application.x_bzip2')
