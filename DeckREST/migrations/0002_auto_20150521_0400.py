# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import DeckREST.models


class Migration(migrations.Migration):

    dependencies = [
        ('DeckREST', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('num', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='deck',
            name='seed',
            field=models.BigIntegerField(default=DeckREST.models.deck_seed),
        ),
        migrations.AddField(
            model_name='deck',
            name='draws',
            field=models.ManyToManyField(to='DeckREST.Card'),
        ),
    ]
