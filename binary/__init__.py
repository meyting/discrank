from otree.api import *


doc = """
Your app description
"""

import pandas as pd
import random
import numpy as np

df1 = pd.read_excel('_static/global/rankrankings/workers_rank_mat.xlsx', keep_default_na = False, engine = 'openpyxl') # can also index sheet by name or fetch all sheets
df2 = pd.read_excel('_static/global/rankrankings/workers_rank_re.xlsx', keep_default_na = False, engine = 'openpyxl') # can also index sheet by name or fetch all sheets

df1["mat_range"] = "middle 4"
df1.loc[(df1.mat_rank <= 4), "mat_range"] = "top 4"
df1.loc[(df1.mat_rank >= 9), "mat_range"] = "bottom 4"
df2["re_range"] = "middle 4"
df2.loc[(df2.re_rank <= 4), "re_range"] = "top 4"
df2.loc[(df2.re_rank >= 9), "re_range"] = "bottom 4"

print("DF1F IN BINARY!",df1f)
print("DF1M IN BINARY!",df1m)

print("DF1 IN BINARY",df1)

df1.to_excel('_static/global/binaryrankings/workers_rank_mat.xlsx')
df2.to_excel('_static/global/binaryrankings/workers_rank_re.xlsx')

class C(BaseConstants):
    NAME_IN_URL = 'binary'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 9
    number_of_workers_tot = 24
    number_of_workers_sep = int(number_of_workers_tot/2)
    number_of_other_subjects = int(number_of_workers_tot-1)
    conversionrate = cu(0.1)
    examplescore = 5
    examplebonus = examplescore * conversionrate

    profiles_mat = [{'prolificid': df1['prolificid'][i],
                     'name': df1['name'][i],
                     'gender':df1['gender'][i],
                     'mat_range': df1["mat_range"][i],
                     'matrices': df1["matrices"][i],
                     'race': df1["race"][i],
                     }
                    for i in range(len(df1))]

    profiles_re = [{'prolificid': df2['prolificid'][i],
                     'name': df2['name'][i],
                     'gender':df2['gender'][i],
                     're_range': df2["re_range"][i],
                     'realeffort': df2["realeffort"][i],
                     'race': df2["race"][i],
                     }
                    for i in range(len(df2))]
    bonus_employer = 50
    flatbonus = cu(2)

class Subsession(BaseSubsession):
    pass

def creating_session(subsession: Subsession):
    for player in subsession.get_players():
        profiles = []
        if player.participant.task == "logic":
            mat_topf_topm = [C.profiles_mat[0], C.profiles_mat[12]]
            random.shuffle(mat_topf_topm)
            profiles.append(mat_topf_topm)
            mat_topf_midm = [C.profiles_mat[1], C.profiles_mat[16]]
            random.shuffle(mat_topf_midm)
            profiles.append(mat_topf_midm)
            mat_topf_botm = [C.profiles_mat[2], C.profiles_mat[20]]
            random.shuffle(mat_topf_botm)
            profiles.append(mat_topf_botm)
            mat_midf_topm = [C.profiles_mat[4], C.profiles_mat[13]]
            random.shuffle(mat_midf_topm)
            profiles.append(mat_midf_topm)
            mat_midf_midm = [C.profiles_mat[5], C.profiles_mat[17]]
            random.shuffle(mat_midf_midm)
            profiles.append(mat_midf_midm)
            mat_midf_botm = [C.profiles_mat[6], C.profiles_mat[21]]
            random.shuffle(mat_midf_botm)
            profiles.append(mat_midf_botm)
            mat_botf_topm = [C.profiles_mat[8], C.profiles_mat[14]]
            random.shuffle(mat_botf_topm)
            profiles.append(mat_botf_topm)
            mat_botf_midm = [C.profiles_mat[9], C.profiles_mat[18]]
            random.shuffle(mat_botf_midm)
            profiles.append(mat_botf_midm)
            mat_botf_botm = [C.profiles_mat[10], C.profiles_mat[22]]
            random.shuffle(mat_botf_botm)
            profiles.append(mat_botf_botm)
        if player.participant.task == "realeffort":
            re_topf_topm = [C.profiles_re[0], C.profiles_re[12]]
            random.shuffle(re_topf_topm)
            profiles.append(re_topf_topm)
            re_topf_midm = [C.profiles_re[1], C.profiles_re[16]]
            random.shuffle(re_topf_midm)
            profiles.append(re_topf_midm)
            re_topf_botm = [C.profiles_re[2], C.profiles_re[20]]
            random.shuffle(re_topf_botm)
            profiles.append(re_topf_botm)
            re_midf_topm = [C.profiles_re[4], C.profiles_re[13]]
            random.shuffle(re_midf_topm)
            profiles.append(re_midf_topm)
            re_midf_midm = [C.profiles_re[5], C.profiles_re[17]]
            random.shuffle(re_midf_midm)
            profiles.append(re_midf_midm)
            re_midf_botm = [C.profiles_re[6], C.profiles_re[21]]
            random.shuffle(re_midf_botm)
            profiles.append(re_midf_botm)
            re_botf_topm = [C.profiles_re[8], C.profiles_re[14]]
            random.shuffle(re_botf_topm)
            profiles.append(re_botf_topm)
            re_botf_midm = [C.profiles_re[9], C.profiles_re[18]]
            random.shuffle(re_botf_midm)
            profiles.append(re_botf_midm)
            re_botf_botm = [C.profiles_re[10], C.profiles_re[22]]
            random.shuffle(re_botf_botm)
            profiles.append(re_botf_botm)
        player.participant.profiles = profiles
        random.shuffle(player.participant.profiles)

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    decision = models.StringField(blank=True)
    decision_race = models.StringField(blank=True)
    offer1 = models.StringField(verbose_name='')
    offer2 = models.StringField(verbose_name='')
    range1 = models.StringField(verbose_name='')
    range2 = models.StringField(verbose_name='')
    score1 = models.StringField(verbose_name='')
    score2 = models.StringField(verbose_name='')
    usedprofiles = models.StringField()

# PAGES
class instructions_binary(Page):
    def is_displayed(player):
        return player.round_number == 1


class binary(Page):
    form_model = 'player'
    form_fields = ['decision', 'offer1', 'offer2', 'range1', 'range2', 'score1', 'score2', 'decision_race']
    def vars_for_template(player):
        if player.participant.task == "logic":
            if player.round_number == 1:
                profile1 = player.participant.profiles[player.round_number-1][0]
                profile2 = player.participant.profiles[player.round_number-1][1]
            if player.round_number == 2:
                profile1 = player.participant.profiles[player.round_number-1][0]
                profile2 = player.participant.profiles[player.round_number-1][1]
            if player.round_number == 3:
                profile1 = player.participant.profiles[player.round_number-1][0]
                profile2 = player.participant.profiles[player.round_number-1][1]
            if player.round_number == 4:
                profile1 = player.participant.profiles[player.round_number-1][0]
                profile2 = player.participant.profiles[player.round_number-1][1]
            if player.round_number == 5:
                profile1 = player.participant.profiles[player.round_number-1][0]
                profile2 = player.participant.profiles[player.round_number-1][1]
            if player.round_number == 6:
                profile1 = player.participant.profiles[player.round_number-1][0]
                profile2 = player.participant.profiles[player.round_number-1][1]
            if player.round_number == 7:
                profile1 = player.participant.profiles[player.round_number-1][0]
                profile2 = player.participant.profiles[player.round_number-1][1]
            if player.round_number == 8:
                profile1 = player.participant.profiles[player.round_number-1][0]
                profile2 = player.participant.profiles[player.round_number-1][1]
            if player.round_number == 9:
                profile1 = player.participant.profiles[player.round_number-1][0]
                profile2 = player.participant.profiles[player.round_number-1][1]
            profile1_id = profile1["prolificid"]  ###### CHANGE TO AN ID  - CREATE ONE FIRST
            profile2_id = profile2["prolificid"]  ###### CHANGE TO AN ID  - CREATE ONE FIRST
            profile1_range = profile1["mat_range"]  ###### CHANGE TO AN ID  - CREATE ONE FIRST
            profile2_range = profile2["mat_range"]  ###### CHANGE TO AN ID  - CREATE ONE FIRST
            profile1_score = profile1["matrices"]  ###### CHANGE TO AN ID  - CREATE ONE FIRST
            profile2_score = profile2["matrices"]  ###### CHANGE TO AN ID  - CREATE ONE FIRST
        if player.participant.task == 'realeffort':
            if player.round_number == 1:
                profile1 = player.participant.profiles[player.round_number-1][0]
                profile2 = player.participant.profiles[player.round_number-1][1]
            if player.round_number == 2:
                profile1 = player.participant.profiles[player.round_number - 1][0]
                profile2 = player.participant.profiles[player.round_number - 1][1]
            if player.round_number == 3:
                profile1 = player.participant.profiles[player.round_number-1][0]
                profile2 = player.participant.profiles[player.round_number-1][1]
            if player.round_number == 4:
                profile1 = player.participant.profiles[player.round_number-1][0]
                profile2 = player.participant.profiles[player.round_number-1][1]
            if player.round_number == 5:
                profile1 = player.participant.profiles[player.round_number-1][0]
                profile2 = player.participant.profiles[player.round_number-1][1]
            if player.round_number == 6:
                profile1 = player.participant.profiles[player.round_number-1][0]
                profile2 = player.participant.profiles[player.round_number-1][1]
            if player.round_number == 7:
                profile1 = player.participant.profiles[player.round_number-1][0]
                profile2 = player.participant.profiles[player.round_number-1][1]
            if player.round_number == 8:
                profile1 = player.participant.profiles[player.round_number-1][0]
                profile2 = player.participant.profiles[player.round_number-1][1]
            if player.round_number == 9:
                profile1 = player.participant.profiles[player.round_number-1][0]
                profile2 = player.participant.profiles[player.round_number-1][1]
            profile1_id = profile1["prolificid"]  ###### CHANGE TO AN ID  - CREATE ONE FIRST
            profile2_id = profile2["prolificid"]  ###### CHANGE TO AN ID  - CREATE ONE FIRST
            profile1_range = profile1["re_range"]  ###### CHANGE TO AN ID  - CREATE ONE FIRST
            profile2_range = profile2["re_range"]  ###### CHANGE TO AN ID  - CREATE ONE FIRST
            profile1_score = profile1["realeffort"]  ###### CHANGE TO AN ID  - CREATE ONE FIRST
            profile2_score = profile2["realeffort"]  ###### CHANGE TO AN ID  - CREATE ONE FIRST

        return {
            'profile1' : profile1,
            'profile2' : profile2,
            'profile1_id' : profile1_id,
            'profile2_id' : profile2_id,
            'profile1_range' : profile1_range,
            'profile2_range' : profile2_range,
            'profile1_score': profile1_score,
            'profile2_score': profile2_score,
            'i1' : '<input name="decision" type="radio" id="w1" value="' + profile1_id + '"' +'/>',
            'i2' : '<input name="decision" type="radio" id="w2" value="' + profile2_id + '"' +'/>',
        }
    def before_next_page(player, timeout_happened):
        player.decision_race = str(df1.loc[(df1.prolificid == player.decision), "race"].values[0])

    def error_message(player, values):
        if values['decision'] == "":
            return 'You forgot to hire a worker. Please click on the worker who you want to hire.'


page_sequence = [instructions_binary,
                 binary
                 ]
