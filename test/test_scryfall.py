import scryfall

def test_client_available():
    assert scryfall.client is not None

def test_card():
    assert scryfall.card.get(1) == 1