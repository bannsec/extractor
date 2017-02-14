#!/usr/bin/env python3

import magic
import sys
import argparse
import logging
import os

from handlers_list import handlers

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("extract")

def main():
    global config

    # Store config data globally
    config = {}

    # Get the commandline input
    parser = argparse.ArgumentParser(description='Universal Extractor')
    parser.add_argument('fileName',metavar='file',type=str,nargs=1,help='The file to extract')
    parser.add_argument('-rm',action='store_true',help='Should we remove the source file after extract? (defualt: False)')

    args = parser.parse_args()

    config['fileName'] = os.path.abspath(args.fileName[0])
 
    logger.info("Got file name: " + config['fileName'])

    config['rm'] = args.rm

    logger.info("Got rm flag of {0}".format(config['rm']))

    # Grab the magic
    config['magic_mime'] = magic.from_file(config['fileName'],mime=True)
    config['magic_str'] = magic.from_file(config['fileName'],mime=False)

    logger.info("File magic is: {0} ({1})".format(config['magic_str'],config['magic_mime']))

    run_extractors()

def run_extractors():
    
    if config['magic_mime'] not in handlers:
        logger.error("No handler available for type {0} ({1})".format(config['magic_str'],config['magic_mime']))
        return

    # Try each handler
    for handler in handlers[config['magic_mime']]:
        handle = handler.handle(config)
        handle.extract()

