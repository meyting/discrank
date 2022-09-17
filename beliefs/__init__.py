from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'beliefs'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    t0 = 0
    t1 = 3
    t2 = 4
    t3 = 6
    t4 = 7
    t5 = 9
    t6 = 10
    t7 = 12
    t8 = 12
    t9 = 15

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    h1 = models.FloatField()
    h2 = models.FloatField()
    h3 = models.FloatField()
    h4 = models.FloatField()
    h5 = models.FloatField()
    hispanictotal = models.FloatField()
    a1 = models.FloatField()
    a2 = models.FloatField()
    a3 = models.FloatField()
    a4 = models.FloatField()
    a5 = models.FloatField()
    asiantotal = models.FloatField()

# PAGES
class beliefs(Page):
    form_model = 'player'
    form_fields = ['h1', 'h2', 'h3', 'h4', 'h5', 'hispanictotal',
                   'a1', 'a2', 'a3', 'a4', 'a5',  'asiantotal',
                   ]

    def error_message(player, value):
        print('value is', value)
        if value["hispanictotal"] != 100:
            return 'Please make sure that the total percentage that you allocated to all hispanic workers sums up to 100%.'
        if value["asiantotal"] != 100:
            return 'Please make sure that the total percentage that you allocated to all asian workers sums up to 100%.'

page_sequence = [beliefs,]
