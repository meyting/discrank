from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'rank'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    checksolution = ["A","B","C","D","E","F","G","H"]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    ranking = models.CharField(blank=True)
    check = models.CharField(blank=True)
    abcdleft = models.CharField(blank=True)
    malesleft = models.CharField(blank=True)


# PAGES
'''
class check(Page):
    form_model = 'player'
    form_fields = ['check',]

    def error_message(player, values):
        checklist = values["check"].split(",")
        if len(checklist) < 8:
            return 'Please add all items to the mixed ranking.'
        if checklist != c.checksolution:
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
        print(checklist)
        print(C.checksolution)
        if len(checklist) < 8:
            return 'Please add all items to the mixed ranking.'
        if checklist != C.checksolution:
            return 'Please make sure that you create the correct mixed ranking: A,B,C,D,E,F,G,H'



class rank2(Page):
    form_model = 'player'
    form_fields = ['ranking',]

    def error_message(player, values):
        rankinglist = values["ranking"].split(",")
        if len(rankinglist) < 30:
            print(len(rankinglist))
            return 'Please add all workers to the mixed ranking.'
'''


class check3(Page):
    form_model = 'player'
    form_fields = ['check', 'abcdleft']

    def error_message(player, values):
        print(values["check"])
        checklist = values["check"].split(",")
        print(checklist)
        if len(checklist) < 8:
            return 'Please add all items to the mixed ranking.'
        if checklist != C.checksolution:
            return 'Please make sure that you create the correct mixed ranking: A,B,C,D,E,F,G,H'

class rank3(Page):
    form_model = 'player'
    form_fields = ['ranking', 'malesleft']

    def error_message(player, values):
        rankinglist = values["ranking"].split(",")
        if len(rankinglist) < 30:
            print(rankinglist)
            return 'Please add all workers to the mixed ranking.'


page_sequence = [#check,
                 #rank,
                 check3,
                 rank3,
                 #check2,
                 #rank2,
]
