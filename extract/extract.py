#!/usr/bin/env python3

import magic
import sys
import argparse
import logging
import os
import importlib
import extract.Colorer

logger = logging.getLogger("extract")

def testLibArchive():
    # Make sure libarchive is installed correctly
    try:
        import libarchive.public
    except:
        logger.error("LibArchive not properly installed. Do the following (for ubuntu):\n\tsudo apt-get install libarchive-dev\n\tpip install https://github.com/dsoprea/PyEasyArchive/tarball/master\n")


def main():
    global config

    # Store config data globally
    config = {}

    # Get the commandline input
    parser = argparse.ArgumentParser(description='Universal Extractor')
    parser.add_argument('fileName',metavar='file',type=str,nargs=1,help='The file to extract')
    parser.add_argument('-rm',action='store_true',help='Should we remove the source file after extract? (defualt: False)')
    parser.add_argument('-debug',action='store_true',help='Enable debugging logging (defualt: False)')

    args = parser.parse_args()

    if args.debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.WARN)

    config['fileName'] = os.path.abspath(args.fileName[0])
 
    logger.info("Got file name: " + config['fileName'])

    config['rm'] = args.rm

    logger.info("Got rm flag of {0}".format(config['rm']))

    # Grab the magic
    config['magic_mime'] = magic.from_file(config['fileName'],mime=True)
    config['magic_str'] = magic.from_file(config['fileName'],mime=False)

    logger.info("File magic is: {0} ({1})".format(config['magic_str'],config['magic_mime']))

    run_extractor()

def run_extractor():

    testLibArchive()
    
    try:
        module = "extract.handlers." + config['magic_mime'].replace("/",".").replace("-","_")
        logger.debug("import " + module)
        handler = importlib.import_module(module)

    except:
        logger.error("No handler available for type {0} ({1})".format(config['magic_str'],config['magic_mime']))
        return

    handle = handler.handle(config)
    handle.extract()

