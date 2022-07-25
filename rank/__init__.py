from otree.api import *


doc = """
Your app description
"""
import pandas as pd

df1 = pd.read_excel('_static/global/workers_rank_mat.xlsx', keep_default_na = False, engine = 'openpyxl') # can also index sheet by name or fetch all sheets
df1 = df1.replace("",999999999)
df2 = pd.read_excel('_static/global/workers_rank_re.xlsx', keep_default_na = False, engine = 'openpyxl') # can also index sheet by name or fetch all sheets
df2 = df2.replace("",999999999)

df1 = df1.sort_values(by=['mat_rank'])
df2 = df2.sort_values(by=['re_rank'])

df1_female = df1[df1.gender=="female"].reset_index()
df1_male = df1[df1.gender=="male"].reset_index()
df2_female = df2[df2.gender=="female"].reset_index()
df2_male = df2[df2.gender=="male"].reset_index()


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

    names_mat_f = [{'name': df1_female['name'][i],
                  'gender': df1_female['gender'][i],
                  'mat_rank': df1_female["mat_rank"][i]
                     }
                  for i in range(len(df1_female))]

    names_mat_m = [{'name': df1_male['name'][i],
                  'gender': df1_male['gender'][i],
                  'mat_rank': df1_male["mat_rank"][i]
                     }
                  for i in range(len(df1_male))]

    names_re_f = [{'name': df2_female['name'][i],
                  'gender': df2_female['gender'][i],
                  're_rank': df2_female["re_rank"][i]
                     }
                  for i in range(len(df2_female))]

    names_re_m = [{'name': df2_male['name'][i],
                  'gender': df2_male['gender'][i],
                  're_rank': df2_male["re_rank"][i]
                  }
                  for i in range(len(df2_male))]

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


class instructions_rank(Page):
    def is_displayed(player):
        return player.round_number == 1


class rank3(Page):
    form_model = 'player'
    form_fields = ['ranking', 'malesleft']

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
