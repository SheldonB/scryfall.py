import logging

import requests

from scryfall import client

log = logging.getLogger('scryfall')

class Card:
    """
    The Card class provides the underlying implementation
    to retrieve card objects from scryfall.
    """

    def test(self):
        return 1

class CardClient:

    CARDS_URI = client.get_base_uri() + '/cards'

    def get_by_multiverse_id(self, multiverse_id):
        uri = self.CARDS_URI + '/multiverse/' + str(multiverse_id)


def get(**kwargs):
    """
    get returns a single card 

    :param id: The Scryfall ID.
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
        log.debug('Getting card based on multiverse id')
        CardClient().get_by_multiverse_id(multiverse_id)

    mtgo_id = kwargs.get('mtgo_id')

    if mtgo_id is not None:
        log.debug('Getting card for mtgo id')

    arena_id = kwargs.get('arena_id')

    if arena_id is not None:
        log.debug('Getting card for arena id')


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
    Retrieves all Cards from Scryfall.

    TODO: This is a paginated request, so we 
    will need to figure out how to handle this.

    A couple ideas:
        - Allow the page number as a param.
        - Use a generator
        - Make it async and just return back when we have all the cards.
    """
    log.debug('Retrieving all cards from Scryfall.')