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
    ranking = models.CharField(blank=True)
    check = models.CharField(blank=True)


# PAGES

class check(Page):
    form_model = 'player'
    form_fields = ['check',]

    def error_message(player, values):
        checklist = values["check"].split(",")
        if len(checklist) < 8:
            return 'Please add all items to the mixed ranking.'


class rank(Page):
    form_model = 'player'
    form_fields = ['ranking',]

    def error_message(player, values):
        rankinglist = values["ranking"].split(",")
        if len(rankinglist) < 30:
            return 'Please add all workers to the mixed ranking.'


class check2(Page):
    form_model = 'player'
    form_fields = ['check',]

    def error_message(player, values):
        checklist = values["check"].split(",")
        if len(checklist) < 8:
            return 'Please add all items to the mixed ranking.'


class rank2(Page):
    form_model = 'player'
    form_fields = ['ranking',]

    def error_message(player, values):
        rankinglist = values["ranking"].split(",")
        if len(rankinglist) < 30:
            print(len(rankinglist))
            return 'Please add all workers to the mixed ranking.'



page_sequence = [#check,
                 #rank,
                 check2,
                 rank2,]
