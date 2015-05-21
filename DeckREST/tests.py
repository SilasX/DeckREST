import unittest

from DeckREST.models import Deck

class TestDeck(unittest.TestCase):

    def test_setup(self):
        deck_obj = Deck()
        self.assertIsNotNone(deck_obj.seed)

    def test_stack_deck(self):
        deck_obj = Deck(seed=400)
        self.assertEquals(400, deck_obj.seed)
        random_card = deck_obj.next_card()
        self.assertEquals(36, random_card)

