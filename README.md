# Install
Just `pip install .`

# Use
Make sure you're in the python environment you installed it to. Then:

```bash
$ extract -h
usage: extract [-h] [-rm] file

Universal Extractor

positional arguments:
  file        The file to extract

optional arguments:
  -h, --help  show this help message and exit
  -rm         Should we remove the source file after extract? (defualt: False)
```

# Extending
Found something that isn't handled? Adding a handler is easy. When extractor fails, it will tell you what the mime type was that it didn't know how to handle:

```bash
$ extract carry.c.lzma 
ERROR:extract:No handler available for type LZMA compressed data, streamed (application/x-lzma)
```

To write a handler, create a module using the mime type. In this case, the mime type is `application/x-lzma`. So, we will create a handler `extract/handlers/application/x_lzma/__init__.py`. This file must define a class named `handle` that extends `handleBaseClass` and exposes an `extract` method. The extract method must call the super class at the end of execution.

Example:

```python
from extract.handlers import handleBaseClass

class handle(handleBaseClass):

    def extract(self):
        config = self.config

        # Open it up
        l = lzma.LZMAFile(config['fileName'])

        # Find the base directory of the file
        directory = os.path.dirname(os.path.abspath(config['fileName']))

        # Do the actual extraction
        with open(config['fileName'] + "_extracted","wb") as f:
            f.write(l.read())

        # Call parent handler
        handleBaseClass.extract(self)
        

import lzma
import logging
import os

logger = logging.getLogger('extract.handlers.application.x_lzma')
```

That's it. The handler will now be automatically discovered and called.

For an example of calling multiple options in sequence, check out [x-compress](extract/handlers/application/x_compress/__init__.py)
