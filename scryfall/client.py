import logging

log = logging.getLogger('scryfall')


class Client:

    BASE_URI = 'https://api.scryfall.com'

    def __init__(self, *args, **kwargs):
        print('Blah')

    def get_base_uri(self):
        return self.BASE_URI

    def configure(self):
        log.debug('Configuring Scryfall.py Client')