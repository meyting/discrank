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
    m1 = models.FloatField()
    m2 = models.FloatField()
    m3 = models.FloatField()
    m4 = models.FloatField()
    m5 = models.FloatField()
    mtotal = models.FloatField()
    f1 = models.FloatField()
    f2 = models.FloatField()
    f3 = models.FloatField()
    f4 = models.FloatField()
    f5 = models.FloatField()
    ftotal = models.FloatField()

    us1 = models.FloatField()
    us2 = models.FloatField()
    us3 = models.FloatField()
    us4 = models.FloatField()
    us5 = models.FloatField()
    ustotal = models.FloatField()
    nus1 = models.FloatField()
    nus2 = models.FloatField()
    nus3 = models.FloatField()
    nus4 = models.FloatField()
    nus5 = models.FloatField()
    nustotal = models.FloatField()

    o1 = models.FloatField()
    o2 = models.FloatField()
    o3 = models.FloatField()
    o4 = models.FloatField()
    o5 = models.FloatField()
    ototal = models.FloatField()
    y1 = models.FloatField()
    y2 = models.FloatField()
    y3 = models.FloatField()
    y4 = models.FloatField()
    y5 = models.FloatField()
    ytotal = models.FloatField()

# PAGES
class beliefs(Page):
    form_model = 'player'
    form_fields = ['m1', 'm2', 'm3', 'm4', 'm5', 'mtotal',
                   'f1', 'f2', 'f3', 'f4', 'f5',  'ftotal',
                   'o1', 'o2', 'o3', 'o4', 'o5', 'ototal',
                   'y1', 'y2', 'y3', 'y4', 'y5', 'ytotal',
                   'us1', 'us2', 'us3', 'us4', 'us5', 'ustotal',
                   'nus1', 'nus2', 'nus3', 'nus4', 'nus5', 'nustotal',
                   ]

    def error_message(player, value):
        print('value is', value)
        if value["mtotal"] != 100:
            return 'Please make sure that the total percentage that you allocated to all male workers sums up to 100%.'
        if value["ftotal"] != 100:
            return 'Please make sure that the total percentage that you allocated to all female workers sums up to 100%.'
        if value["ototal"] != 100:
            return 'Please make sure that the total percentage that you allocated to all old workers sums up to 100%.'
        if value["ytotal"] != 100:
            return 'Please make sure that the total percentage that you allocated to all young workers sums up to 100%.'
        if value["ustotal"] != 100:
            return 'Please make sure that the total percentage that you allocated to all US-workers sums up to 100%.'
        if value["nustotal"] != 100:
            return 'Please make sure that the total percentage that you allocated to all Non-US-workers sums up to 100%.'

page_sequence = [beliefs,]
