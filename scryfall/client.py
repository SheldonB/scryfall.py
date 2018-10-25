import logging

log = logging.getLogger('scryfall')

class Client:
    def __init__(self, *args, **kwargs):
        print('Blah')

    def configure(self):
        log.debug('Configuring Scryfall.py Client')