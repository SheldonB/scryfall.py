import scryfall

def test_client_available():
    assert scryfall.client is not None

def test_get_by_multiverse_id():
    scryfall.card.get(multiverse_id=409574)