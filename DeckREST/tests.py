from django.test import TestCase

from DeckREST.models import Card, Deck

class TestDeck(TestCase):

    fixtures = ['simpledeck.json']
    # Note: for seed=400, card order should be:
    # 32, 5, 48, 29, 44 ...

    def test_stack_deck(self):
        deck_obj = Deck(seed=400)
        deck_obj.save()
        self.assertEquals(400, deck_obj.seed)
        random_card = deck_obj.next_card()
        self.assertEquals(32, random_card.num)

    def test_draws_mult(self):
        deck_obj = Deck(seed=400)
        deck_obj.save()
        random_card = deck_obj.next_card()
        self.assertEquals(32, random_card.num)
        expected = set([32, 5])
        deck_obj.remove_card(32)
        deck_obj.remove_card(5)
        deck_obj.remove_card(5)
        actual = set([x.num for x in deck_obj.draws.all()])
        self.assertEquals(expected, actual)
        # Then check that the next card is 48
        self.assertEquals(48, deck_obj.next_card().num)
