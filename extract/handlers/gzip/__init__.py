from extract.handlers import handleBaseClass

class handle(handleBaseClass):

    def extract(self):
        config = self.config

        # Open it up
        g = gzip.GzipFile(config['fileName'])

        # Find the base directory of the file
        directory = os.path.dirname(os.path.abspath(config['fileName']))
        
        # Do the actual extraction
        # TODO: Maybe we wanna buffer this...
        with open(config['fileName'] + "_extracted","wb") as f:
            f.write(g.read())

        # Call parent handler
        handleBaseClass.extract(self)
        
        
import gzip
import logging
import os

logger = logging.getLogger('extract.handlers.gzip')
