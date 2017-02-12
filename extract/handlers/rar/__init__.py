from extract.handlers import handleBaseClass

class handle(handleBaseClass):

    # TODO: Reimplement trying different extractors in preference: 7z, unrar-nonfree, rarfile

    def extract(self):
        config = self.config

        # Open it up
        r = rarfile.RarFile(config['fileName'],crc_check=False)

        logger.info("Extracting the following files: {0}".format(r.namelist()))

        # Find the base directory of the file
        directory = os.path.dirname(os.path.abspath(config['fileName']))

        # Do the actual extraction
        r.extractall(path=directory)

        # Call parent handler
        handleBaseClass.extract(self)

import rarfile
import logging
import os

logger = logging.getLogger('extract.handlers.rar')
