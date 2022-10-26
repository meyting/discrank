from otree.api import *


doc = """
Your app description
"""
import pandas as pd
import random
import numpy as np

df1 = pd.read_excel('_static/global/workers_rank_mat.xlsx', keep_default_na = False, engine = 'openpyxl') # can also index sheet by name or fetch all sheets
df1 = df1.replace("",999999999)
random.seed(0)
df1['random'] = np.random.uniform(0, 0.5, df1.shape[0])
df1.matrices = df1.matrices+df1["random"]
df2 = pd.read_excel('_static/global/workers_rank_re.xlsx', keep_default_na = False, engine = 'openpyxl') # can also index sheet by name or fetch all sheets
df2 = df2.replace("",999999999)
random.seed(0)
df2['random'] = np.random.uniform(0, 0.5, df2.shape[0])
df2.realeffort = df2.realeffort+df2["random"]
df1['race'] = df1['race'].replace({'Hispanic or Latin':'Hispanic'})
df2['race'] = df2['race'].replace({'Hispanic or Latin':'Hispanic'})

df1f = df1[df1.gender=="female"].reset_index()
df1m = df1[df1.gender=="male"].reset_index()
df2f = df2[df2.gender=="female"].reset_index()
df2m = df2[df2.gender=="male"].reset_index()

df1f = df1f[["prolificid", "name", "gender", "matrices", "race"]].sample(n=12, random_state = 1)
df1m = df1m[["prolificid", "name", "gender", "matrices", "race"]].sample(n=12, random_state = 1)
df2f = df2f[["prolificid", "name", "gender", "realeffort", "race"]].sample(n=12, random_state = 1)
df2m = df2m[["prolificid", "name", "gender", "realeffort", "race"]].sample(n=12, random_state = 1)

df1m["mat_rank"] = df1m.matrices.rank(ascending=False)
df1f["mat_rank"] = df1f.matrices.rank(ascending=False)
df2m["re_rank"] = df2m.realeffort.rank(ascending=False)
df2f["re_rank"] = df2f.realeffort.rank(ascending=False)

df1m = df1m.sort_values(by=['mat_rank']).reset_index()
df1f = df1f.sort_values(by=['mat_rank']).reset_index()
df2m = df2m.sort_values(by=['re_rank']).reset_index()
df2f = df2f.sort_values(by=['re_rank']).reset_index()

df1f.to_excel('_static/global/rankrankings/workers_rank_mat_female.xlsx')
df1m.to_excel('_static/global/rankrankings/workers_rank_mat_male.xlsx')
df2f.to_excel('_static/global/rankrankings/workers_rank_re_female.xlsx')
df2m.to_excel('_static/global/rankrankings/workers_rank_re_male.xlsx')

df1 = pd.concat([df1f, df1m], axis=0).reset_index()
df2 = pd.concat([df2f, df2m], axis=0).reset_index()

df1.to_excel('_static/global/rankrankings/workers_rank_mat.xlsx')
df2.to_excel('_static/global/rankrankings/workers_rank_re.xlsx')

print("DF1F IN RANK!",df1f)
print("DF1M IN RANK!",df1m)

print("DF1 IN RANK",df1)
class C(BaseConstants):
    NAME_IN_URL = 'rank'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    checksolution = ["A","B","C","D","E","F","G","H"]
    number_of_workers_tot = 24
    number_of_workers_sep = int(number_of_workers_tot/2)
    number_of_other_subjects = int(number_of_workers_tot-1)
    conversionrate = cu(0.1)
    examplescore = 5
    examplebonus = examplescore * conversionrate

    names_mat_f = [{'name': df1f['name'][i],
                    'gender': df1f['gender'][i],
                    'mat_rank': df1f["mat_rank"][i],
                    'race': df1f["race"][i],
                     }
                  for i in range(len(df1f))]

    names_mat_m = [{'name': df1m['name'][i],
                   'gender': df1m['gender'][i],
                   'mat_rank': df1m["mat_rank"][i],
                   'race': df1m["race"][i],
                    }
                  for i in range(len(df1m))]

    names_re_f = [{'name': df2f['name'][i],
                   'gender': df2f['gender'][i],
                   're_rank': df2f["re_rank"][i],
                   'race': df2f["race"][i],
                   }
                  for i in range(len(df2f))]

    names_re_m = [{'name': df2m['name'][i],
                   'gender': df2m['gender'][i],
                   're_rank': df2m["re_rank"][i],
                   'race': df2m["race"][i],
                   }
                  for i in range(len(df2m))]

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    ranking = models.CharField(blank=True)
    check = models.CharField(blank=True)
    abcdleft = models.CharField(blank=True)
    malesleft = models.CharField(blank=True)
    femaleranking_mat = models.CharField()
    femaleranking_re = models.CharField()
    maleranking_mat = models.CharField()
    maleranking_re = models.CharField()


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


class instructions_rank(Page):
    def is_displayed(player):
        return player.round_number == 1


class rank3(Page):
    form_model = 'player'
    form_fields = ['ranking', 'malesleft']

    def vars_for_template(player):
        player.femaleranking_mat = str(C.names_mat_f)
        player.maleranking_mat = str(C.names_mat_m)
        player.femaleranking_re = str(C.names_re_f)
        player.maleranking_re = str(C.names_re_m)

    def error_message(player, values):
        rankinglist = values["ranking"].split(",")
        if len(rankinglist) < C.number_of_workers_tot:
            print(rankinglist)
            return 'Please add all workers to the mixed ranking.'


    def js_vars(player):
        if player.participant.task == 'logic':
            names_f = [C.names_mat_f[i]["name"] for i in range(len(C.names_mat_f))]
            names_m = [C.names_mat_m[i]["name"] for i in range(len(C.names_mat_m))]
        if player.participant.task == 'realeffort':
            names_f = [C.names_re_f[i]["name"] for i in range(len(C.names_re_f))]
            names_m = [C.names_re_m[i]["name"] for i in range(len(C.names_re_m))]
        return dict(
            female1=names_f[0],
            female2=names_f[1],
            female3=names_f[2],
            female4=names_f[3],
            female5=names_f[4],
            female6=names_f[5],
            female7=names_f[6],
            female8=names_f[7],
            female9=names_f[8],
            female10=names_f[9],
            female11=names_f[10],
            female12=names_f[11],
            male1=names_m[0],
            male2=names_m[1],
            male3=names_m[2],
            male4=names_m[3],
            male5=names_m[4],
            male6=names_m[5],
            male7=names_m[6],
            male8=names_m[7],
            male9=names_m[8],
            male10=names_m[9],
            male11=names_m[10],
            male12=names_m[11],
                )


page_sequence = [instructions_rank,
                 check3,
                 rank3,
                 ]
