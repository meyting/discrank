from otree.api import *


doc = """
Your app description
"""

import pandas as pd

df_real = pd.read_excel('_static/global/targetpool_us_real.xlsx', keep_default_na = False, engine = 'openpyxl') # can also index sheet by name or fetch all sheets
df_neutral = pd.read_excel('_static/global/targetpool_us_neutral.xlsx', keep_default_na = False, engine = 'openpyxl') # can also index sheet by name or fetch all sheets
df_neutral = df_neutral.replace("",999999999)
df_neutral["age"] = df_neutral["age"].astype(float)
df_neutral["total"] = df_neutral["total"].astype(float)
df_neutral["maths_hs"] = df_neutral["maths_hs"].astype(float)
df_neutral["english_hs"] = df_neutral["english_hs"].astype(float)
df_neutral["amb"] = df_neutral["amb"].astype(float)
df_neutral["ver"] = df_neutral["ver"].astype(float)
df_neutral["res"] = df_neutral["res"].astype(float)
df_neutral["gew"] = df_neutral["gew"].astype(float)
df_neutral["act"] = df_neutral["act"].astype(float)
df_neutral["sat"] = df_neutral["sat"].astype(float)
df_neutral["actsat"] = df_neutral["actsat"].astype(float)
df_neutral = df_neutral.replace(999999999, "N/A")



class C(BaseConstants):
    NAME_IN_URL = 'binary'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 7

    all_profiles = [{'prolificid': df_neutral['prolificid'][i],
                     'name': df_neutral['name'][i],
                     'gender':df_neutral['gender'][i]
                     }
                    for i in range(num_rounds*2)]
    usedprofiles = all_profiles

    bonus_employer = 50
    flatbonus = c(2)

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    decision = models.StringField(blank=True)
    offer1 = models.StringField(widget=widgets.HiddenInput(), verbose_name='')
    offer2 = models.StringField(widget=widgets.HiddenInput(), verbose_name='')
    worker1_id = models.StringField()
    worker2_id = models.StringField()


# PAGES
class binary(Page):
    form_model = 'player'
    form_fields = ['decision', 'offer1', 'offer2']

    def vars_for_template(self):
        profile1 = self.player.participant.vars["usedprofiles"][self.round_number + self.round_number - 2]
        profile2 = self.player.participant.vars["usedprofiles"][self.round_number + self.round_number - 1]
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

    def error_message(self, values):
        if values['decision'] == None:
            return 'You forgot to hire a worker. Please click on the worker who you want to hire.'



page_sequence = [binary]
