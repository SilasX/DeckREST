import random

from django.db import models

def deck_seed():
    return random.randint(-9223372036854775808, 9223372036854775807)

class Card(models.Model):
    num = models.IntegerField()  # Number 0-51 indicating card identity

class Deck(models.Model):
    seed = models.BigIntegerField(default=deck_seed)
    draws = models.ManyToManyField(Card)

    def next_card(self):
        return self.seed % 52

    def remove_card(self, num):
        """ensure a specific card is removed, identified by its integer
`num` (0-51)"""
        target_card = Card.objects.get(num=num)
        if target_card not in self.draws.all():
            self.draws.add(target_card)
            self.save()
