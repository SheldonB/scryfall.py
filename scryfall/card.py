import logging
from scryfall import client

log = logging.getLogger('scryfall')

class Card:
    """
    The Card class provides the underlying implementation
    to retrieve card objects from scryfall.
    """

    def test(self):
        return 1


def get(**kwargs):
    """
    get returns a single card 

    :param id: The
    :param multiverse_id: The Card objects multiverse ID.
    :param mtgo_id: The card objects MTGO ID.
    :param arena_id: The card objects MtG Arena ID.
    """
    if kwargs is None:
        log.warn('No Arguments specified. To get all cards call card.all()')
        return

    scryfall_id = kwargs.get('id')

    if scryfall_id is not None:
        log.debug('Getting card based on scryfall id')
        return

    multiverse_id = kwargs.get('multiverse_id')

    if multiverse_id is not None:
        log.debug('Getting card based on multivers id')


def search(**kwargs):
    """
    Returns a list of cards for the search
    criteria. If no cards match, then return None
    """
    log.debug('Testing Search.')


def random():
    """
    Return a random card from Scryfall.
    """
    log.debug('Testing Random')


def all():
    """
    Retrieves all Cards from Scryfall
    """
    log.debug('Retrieving all cards from Scryfall.')