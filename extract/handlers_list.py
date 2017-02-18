import handlers.zip
import handlers.rar
import handlers.tar
import handlers.gzip
import handlers.bzip2

# Dictionary of lists of objects to use to unpack
handlers = {
    'application/zip'  : [handlers.zip],
    'application/x-rar': [handlers.rar],
    'application/x-tar': [handlers.tar],
    'application/gzip' : [handlers.gzip],
    'application/x-bzip2': [handlers.bzip2],
}
