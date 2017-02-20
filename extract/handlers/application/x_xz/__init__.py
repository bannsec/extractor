from extract.handlers import handleBaseClass

class handle(handleBaseClass):

    def extract(self):
        config = self.config

        # Open it up
        l = lzma.LZMAFile(config['fileName'])

        # Find the base directory of the file
        directory = os.path.dirname(os.path.abspath(config['fileName']))

        # Determine output file name
        if config['fileName'].endswith(".xz"):
            outFile = config['fileName'][:-3]
        else:
            outFile = config['fileName'] + "_extracted"
        
        # Do the actual extraction
        with open(outFile,"wb") as f:
            f.write(l.read())

        # Call parent handler
        handleBaseClass.extract(self)
        

import lzma
import logging
import os

logger = logging.getLogger('extract.handlers.application.x_xz')
