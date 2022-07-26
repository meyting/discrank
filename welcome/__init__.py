from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'welcome'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass

def creating_session(subsession: Subsession):
    import itertools
    task = itertools.cycle(['logic', 'realeffort'])
    for player in subsession.get_players():
        if 'task' in subsession.session.config:
            player.participant.task = subsession.session.config['task']
        else:
            player.participant.task = next(task)
        player.task = player.participant.task
        print("MMMMMMMMMMMMM",player.participant.task)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    task = models.CharField()
    consent = models.BooleanField()

# PAGES
class consent(Page):
    form_model = 'player'
    form_fields = ['consent']

class instructions(Page):
    pass

page_sequence = [consent,
                 instructions]
