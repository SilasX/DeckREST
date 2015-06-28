import random

from django.db import models

def deck_seed():
    return random.randint(-9223372036854775808, 9223372036854775807)

class Card(models.Model):
    num = models.IntegerField()  # Number 0-51 indicating card identity

class Deck(models.Model):
    DECK_SIZE = 52
    seed = models.BigIntegerField(default=deck_seed)
    draws = models.ManyToManyField(Card)

    def _cards_left(self):
        return self.DECK_SIZE - self.draws.count()

    def _card_order(self):
        random.seed(self.seed)
        card_list = range(Card.objects.count())
        random.shuffle(card_list)
        return card_list

    def next_card(self):
        """Return the card that would be drawn next
        """
        cards_left =  self._cards_left()
        if cards_left == 0:
            raise Exception
        card_num = self._card_order()[self.DECK_SIZE - cards_left]
        return Card.objects.get(num=card_num)

    def remove_card(self, num):
        """ensure a specific card is removed, identified by its integer
`num` (0-51)"""
        target_card = Card.objects.get(num=num)
        if target_card not in self.draws.all():
            self.draws.add(target_card)
            self.save()
