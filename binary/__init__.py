from otree.api import *


doc = """
Your app description
"""

import pandas as pd

df1 = pd.read_excel('_static/global/workers_binary_mat.xlsx', keep_default_na = False, engine = 'openpyxl') # can also index sheet by name or fetch all sheets
df1 = df1.replace("",999999999)
df2 = pd.read_excel('_static/global/workers_binary_re.xlsx', keep_default_na = False, engine = 'openpyxl') # can also index sheet by name or fetch all sheets
df2 = df2.replace("",999999999)

class C(BaseConstants):
    NAME_IN_URL = 'binary'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 7

    profiles_mat = [{'prolificid': df1['prolificid'][i],
                     'name': df1['name'][i],
                     'gender':df1['gender'][i],
                     'mat_range': df1["mat_range"][i],
                     're_range': df1["re_range"][i]
                     }
                    for i in range(NUM_ROUNDS*2)]

    profiles_re = [{'prolificid': df2['prolificid'][i],
                     'name': df2['name'][i],
                     'gender':df2['gender'][i],
                     'mat_range': df2["mat_range"][i],
                     're_range': df2["re_range"][i],
                     }
                    for i in range(NUM_ROUNDS*2)]
    bonus_employer = 50
    flatbonus = cu(2)

class Subsession(BaseSubsession):
    pass

def creating_session(subsession: Subsession):
    for player in subsession.get_players():
        if player.participant.task== "logic":
            player.worker1_id = C.profiles_mat[player.round_number + player.round_number - 2]["prolificid"]
            player.worker2_id = C.profiles_mat[player.round_number + player.round_number - 1]["prolificid"]
        if player.participant.task== "realeffort":
            player.worker1_id = C.profiles_re[player.round_number + player.round_number - 2]["prolificid"]
            player.worker2_id = C.profiles_re[player.round_number + player.round_number - 1]["prolificid"]

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    decision = models.StringField(blank=True)
    decision_gender = models.StringField(blank=True)
    offer1 = models.StringField(verbose_name='')
    offer2 = models.StringField(verbose_name='')
    worker1_id = models.StringField()
    worker2_id = models.StringField()
    usedprofiles = models.StringField()


# PAGES
class binary(Page):
    form_model = 'player'
    form_fields = ['decision', 'offer1', 'offer2','decision_gender']

    def vars_for_template(player):
        if player.participant.task == 'logic':
            profile1 = C.profiles_mat[player.round_number + player.round_number - 2]
            profile2 = C.profiles_mat[player.round_number + player.round_number - 1]
            profile1_id = profile1["prolificid"] ###### CHANGE TO AN ID  - CREATE ONE FIRST
            profile2_id = profile2["prolificid"] ###### CHANGE TO AN ID  - CREATE ONE FIRST
        if player.participant.task == 'realeffort':
            profile1 = C.profiles_re[player.round_number + player.round_number - 2]
            profile2 = C.profiles_re[player.round_number + player.round_number - 1]
            profile1_id = profile1["prolificid"] ###### CHANGE TO AN ID  - CREATE ONE FIRST
            profile2_id = profile2["prolificid"] ###### CHANGE TO AN ID  - CREATE ONE FIRST
        return {
            'profile1' : profile1,
            'profile2' : profile2,
            'profile1_id' : profile1_id,
            'profile2_id' : profile2_id,
            'i1' : '<input name="decision" type="radio" id="w1" value="' + profile1_id + '"' +'/>',
            'i2' : '<input name="decision" type="radio" id="w2" value="' + profile2_id + '"' +'/>',
        }

    def before_next_page(player, timeout_happened):
        player.decision_gender = str(df1.loc[(df1.prolificid == player.decision), "gender"].values[0])

    def error_message(player, values):
        if values['decision'] == "":
            return 'You forgot to hire a worker. Please click on the worker who you want to hire.'



page_sequence = [binary]
