from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'beliefs'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    t0 = 0
    t1 = 5
    t2 = 6
    t3 = 10
    t4 = 11
    t5 = 15
    t6 = 16
    t7 = 20
    t8 = 21
    t9 = 25
    t10 = 26
    t11 = 30

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    m1 = models.FloatField()
    m2 = models.FloatField()
    m3 = models.FloatField()
    m4 = models.FloatField()
    m5 = models.FloatField()
    m6 = models.FloatField()
    mtotal = models.FloatField()
    f1 = models.FloatField()
    f2 = models.FloatField()
    f3 = models.FloatField()
    f4 = models.FloatField()
    f5 = models.FloatField()
    f6 = models.FloatField()
    ftotal = models.FloatField()

# PAGES
class beliefs(Page):
    form_model = 'player'
    form_fields = ['m1', 'm2', 'm3', 'm4', 'm5', 'm6', 'mtotal',
                   'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'ftotal',
                   ]

    def error_message(player, value):
        print('value is', value)
        if value["mtotal"] != 100:
            return 'Please make sure that the total percentage that you allocated to all male workers sums up to 100%.'
        if value["ftotal"] != 100:
            return 'Please make sure that the total percentage that you allocated to all female workers sums up to 100%.'

page_sequence = [beliefs,]
