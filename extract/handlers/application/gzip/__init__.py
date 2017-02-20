from extract.handlers import handleBaseClass

class handle(handleBaseClass):

    def extract(self):
        config = self.config

        # Open it up
        g = gzip.GzipFile(config['fileName'])

        # Find the base directory of the file
        directory = os.path.dirname(os.path.abspath(config['fileName']))

        # Determine output file name
        if config['fileName'].endswith(".gz"):
            outFile = config['fileName'][:-3]
        else:
            outFile = config['fileName'] + "_extracted"
        
        # Do the actual extraction
        # TODO: Maybe we wanna buffer this...
        with open(outFile,"wb") as f:
            f.write(g.read())

        # Call parent handler
        handleBaseClass.extract(self)
        
        
import gzip
import logging
import os

logger = logging.getLogger('extract.handlers.application.gzip')
