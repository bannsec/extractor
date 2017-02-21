from extract.handlers import handleBaseClass

class handle(handleBaseClass):

    def _libarchive(self):
        try:
            # Do the actual extraction
            with open(config['fileName'],"rb") as f:                                            
                for entry in libarchive.public.memory_pour(f.read()):
                    pass
            return True

        except:
            return False
        
    def _lzop(self):
        config = self.config

        # Are we dealing with LZOP?
        if "lzop compressed data" not in config['magic_str'].lower():
            logger.info("Doesn't appear to be LZOP")
            return False

        # Do we have the tool installed?
        if not shutil.which("lzop"):
            logger.warn("lzop isn't installed. try installing it")
            return False

        try:
            subprocess.check_output(["lzop","-d","-f",self.config['fileName']])
            return True

        except:
            return False

    def _zpaq(self):
        config = self.config

        # Are we dealing with ZPAQ?
        if "zpaq" not in config['magic_str'].lower():
            logger.info("Doesn't appear to be ZPAQ")
            return False

        # Do we have the tool installed?
        if not shutil.which("zpaq"):
            logger.warn("zpaq isn't installed. try installing it")
            return False

        # TODO: Only way of checking for errors here is brittle..
        out = subprocess.check_output(["zpaq","x",self.config['fileName']])

        if b"0 file(s) extracted" in out or b"Error" in out:
            logger.warn("Possible error using zpaq: " + out.decode('ascii'))
            return False

        return True

    def _nufile(self):
        config = self.config

        # Are we dealing with NuFile?
        if "nufile" not in config['magic_str'].lower():
            logger.info("Doesn't appear to be NuFile")
            return False

        # Do we have the tool installed?
        if not shutil.which("nulib2"):
            logger.warn("nulib2 isn't installed. try installing it (http://nulib.com/downloads/index.htm)")
            return False

        try:
            subprocess.check_output(["nulib2","-xs",config['fileName']])
            return True

        except Exception as e:
            logger.error("Something went wrong with nulib extraction\n\t" + e.output)
            return False

    def _dact(self):
        config = self.config

        # Are we dealing with DACT?
        with open(config['fileName'],"rb") as f:
            if f.read(3) != b"DCT":
                logger.info("Doesn't appear to be DACT")
                return False
        
        # Do we have the tool?
        if not shutil.which("dact"):
            logger.warn("dact isn't installed. try installing it.")
            return False

        out = subprocess.check_output(["dact","-df",config['fileName']],stderr=subprocess.STDOUT)
        
        if out != b"":
            logger.error("DACT might have errored:\n\t" + out)
            return False

        return True

    def extract(self):
        # List of preferred extraction options
        extract_options = [
            self._libarchive,
            self._lzop,
            self._zpaq,
            self._nufile,
            self._dact,
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
import libarchive.public
import subprocess
import shutil

logger = logging.getLogger('extract.handlers.application.octet_stream')
