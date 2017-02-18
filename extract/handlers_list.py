import handlers.zip
import handlers.rar
import handlers.tar
import handlers.gzip

# Dictionary of lists of objects to use to unpack
handlers = {
    'application/zip'  : [handlers.zip],
    'application/x-rar': [handlers.rar],
    'application/x-tar': [handlers.tar],
    'application/gzip' : [handlers.gzip],
}
