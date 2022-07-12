from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'rank'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    ranking = models.CharField()


# PAGES
class rank(Page):
    form_model = 'player'
    form_fields = ['ranking',]



page_sequence = [rank,]
