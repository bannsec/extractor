from extract.handlers import handleBaseClass

class handle(handleBaseClass):

    def _arj(self):
        if not shutil.which("arj"):
            logger.error("arj not found. try installing it")
            return False

        try:
            subprocess.check_output(["arj","x","-y",self.config['fileName']])
            return True

        except:
            return False


    def extract(self):
        # List of preferred extraction options
        extract_options = [
            self._arj,
        ]

        config = self.config

        # Find the base directory of the file
        directory = os.path.dirname(os.path.abspath(config['fileName']))

        # Default to extracting to the same directory
        os.chdir(directory)

        # Try different options
        if not any(option() for option in extract_options):
            logger.error("Extraction attempts failed!")
            # Return before we accidentally remove the file
            return False

        # Call parent handler
        handleBaseClass.extract(self)
        

import logging
import os
import subprocess
import shutil

logger = logging.getLogger('extract.handlers.application.x_arj')
