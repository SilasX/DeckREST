import random

from django.db import models

def deck_seed():
    return random.randint(-9223372036854775808, 9223372036854775807)


class Deck(models.Model):
    seed = models.BigIntegerField(default=deck_seed)

    def next_card(self):
        return self.seed % 52
