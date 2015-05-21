import unittest

from DeckREST.models import Card, Deck

class TestDeck(unittest.TestCase):

    def setUp(self):
        for n in xrange(52):
            crd = Card(num=n)
            crd.save()

    def test_stack_deck(self):
        deck_obj = Deck(seed=400)
        self.assertEquals(400, deck_obj.seed)
        random_card = deck_obj.next_card()
        self.assertEquals(36, random_card)

    def test_draws_mult(self):
        deck_obj = Deck(seed=400)
        deck_obj.save()
        expected = set([36, 37])
        deck_obj.remove_card(36)
        deck_obj.remove_card(36)
        deck_obj.remove_card(37)
        actual = set([x.num for x in deck_obj.draws.all()])
        self.assertEquals(expected, actual)
