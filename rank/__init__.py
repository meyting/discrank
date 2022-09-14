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

df1h = df1[df1.race=="Hispanic"].reset_index()
df1a = df1[df1.race=="Asian"].reset_index()
df2h = df2[df2.race=="Hispanic"].reset_index()
df2a = df2[df2.race=="Asian"].reset_index()

df1h = df1h[["name", "gender", "matrices", "race"]].sample(n=12, random_state = 1)
df1a = df1a[["name", "gender", "matrices", "race"]].sample(n=12, random_state = 1)
df2h = df2h[["name", "gender", "realeffort", "race"]].sample(n=12, random_state = 1)
df2a = df2a[["name", "gender", "realeffort", "race"]].sample(n=12, random_state = 1)

df1h["mat_rank"] = df1h.matrices.rank(ascending=False)
df1a["mat_rank"] = df1a.matrices.rank(ascending=False)
df2h["re_rank"] = df2h.realeffort.rank(ascending=False)
df2a["re_rank"] = df2a.realeffort.rank(ascending=False)

df1h = df1h.sort_values(by=['mat_rank']).reset_index()
df1a = df1a.sort_values(by=['mat_rank']).reset_index()
df2h = df2h.sort_values(by=['re_rank']).reset_index()
df2a = df2a.sort_values(by=['re_rank']).reset_index()


df1h.to_csv('_static/global/rankrankings/workers_rank_mat_hispanic.csv')
df1a.to_csv('_static/global/rankrankings/workers_rank_mat_asian.csv')
df2h.to_csv('_static/global/rankrankings/workers_rank_re_hispanic.csv')
df2a.to_csv('_static/global/rankrankings/workers_rank_re_asian.csv')

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

    names_mat_a = [{'name': df1a['name'][i],
                    'gender': df1a['gender'][i],
                    'mat_rank': df1a["mat_rank"][i],
                    'race': df1a["race"][i],
                     }
                  for i in range(len(df1a))]

    names_mat_h = [{'name': df1h['name'][i],
                   'gender': df1h['gender'][i],
                   'mat_rank': df1h["mat_rank"][i],
                   'race': df1h["race"][i],

                    }
                  for i in range(len(df1h))]

    names_re_a = [{'name': df2a['name'][i],
                   'gender': df2a['gender'][i],
                   're_rank': df2a["re_rank"][i],
                   'race': df2a["race"][i],
                   }
                  for i in range(len(df2a))]

    names_re_h = [{'name': df2h['name'][i],
                   'gender': df2h['gender'][i],
                   're_rank': df2h["re_rank"][i],
                   'race': df2h["race"][i],
                   }
                  for i in range(len(df2h))]

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    ranking = models.CharField(blank=True)
    check = models.CharField(blank=True)
    abcdleft = models.CharField(blank=True)
    asiansleft = models.CharField(blank=True)
    asianranking_mat = models.CharField()
    asianranking_re = models.CharField()
    hispanicranking_mat = models.CharField()
    hispanicranking_re = models.CharField()


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
    form_fields = ['ranking', 'asiansleft']

    def vars_for_template(player):
        player.hispanicranking_mat = str(C.names_mat_h)
        player.asianranking_mat = str(C.names_mat_a)
        player.hispanicranking_re = str(C.names_re_h)
        player.asianranking_re = str(C.names_re_a)

    def error_message(player, values):
        rankinglist = values["ranking"].split(",")
        if len(rankinglist) < C.number_of_workers_tot:
            print(rankinglist)
            return 'Please add all workers to the mixed ranking.'

    def js_vars(player):
        if player.participant.task == 'logic':
            names_h = [C.names_mat_h[i]["name"] for i in range(len(C.names_mat_h))]
            names_a = [C.names_mat_a[i]["name"] for i in range(len(C.names_mat_a))]
        if player.participant.task == 'realeffort':
            names_h = [C.names_re_h[i]["name"] for i in range(len(C.names_re_h))]
            names_a = [C.names_re_a[i]["name"] for i in range(len(C.names_re_a))]
        return dict(
            asian1=names_a[0],
            asian2=names_a[1],
            asian3=names_a[2],
            asian4=names_a[3],
            asian5=names_a[4],
            asian6=names_a[5],
            asian7=names_a[6],
            asian8=names_a[7],
            asian9=names_a[8],
            asian10=names_a[9],
            asian11=names_a[10],
            asian12=names_a[11],
            hispanic1=names_h[0],
            hispanic2=names_h[1],
            hispanic3=names_h[2],
            hispanic4=names_h[3],
            hispanic5=names_h[4],
            hispanic6=names_h[5],
            hispanic7=names_h[6],
            hispanic8=names_h[7],
            hispanic9=names_h[8],
            hispanic10=names_h[9],
            hispanic11=names_h[10],
            hispanic12=names_h[11],
                )


page_sequence = [instructions_rank,
                 check3,
                 rank3,
                 ]
