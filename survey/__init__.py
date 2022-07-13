from otree.api import *


doc = """
Your app description
"""
import pandas as pd

df = pd.read_excel('_static/global/choices.xlsx', engine = 'openpyxl') # can also index sheet by name or fetch all sheets
countries = df['country'][0:196].tolist()
nationalities = df['nationality'][0:225].tolist()
states = df['states'][0:50].tolist()


class C(BaseConstants):
    NAME_IN_URL = 'survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    choices_hs = [[15, 'A++'], [14, 'A+'], [13, 'A'], [12, 'A-'], [11, 'B+'], [10, 'B'], [9, 'B-'], [8, 'C+'],
                  [7, 'C'], [6, 'C-'], [5, 'D+'], [4, 'D'], [3, 'D-'], [2, 'F']]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    birthday = models.CharField(verbose_name='Please provide your date of birth:')
    gender = models.CharField(initial=None,
                              choices=['female', 'male', 'non-binary'],
                              verbose_name='What is your gender?',
                              widget=widgets.RadioSelect())
    nationality = models.CharField(initial=None,
                                   choices=nationalities,
                                   verbose_name='What is your nationality? (If you possess more than one nationality, please provide the one with which you identify the most.)')
    state = models.CharField(initial=None,
                             choices=states,
                             verbose_name='Which state do you currently live in?')
    occupation = models.IntegerField(initial=None)
    education = models.CharField(initial=None,
                                 verbose_name='What is your highest achieved level of education?',
                                 choices=['Did not graduate high school', 'High school or GED',
                                          'Began college, no degree yet', 'Bachelor', 'Associate', 'Master',
                                          'Doctoral', 'other'], )
    fieldofstudy = models.CharField(initial=None,
                                    blank=True,
                                    verbose_name='What do you study?',
                                    )
    profession = models.CharField(initial=None,
                                  blank=True,
                                  verbose_name='What job do you work in?')

    religion = models.CharField(initial=None,
                                verbose_name='To which religious group do you belong?',
                                choices=['Catholic', 'Protestant', 'Mormon',
                                         'Atheist', 'Jewish', 'Muslim', 'Hindu',
                                         'Buddhist', 'other'], )
    race = models.CharField(initial=None,
                            verbose_name="What is your race/ethnicity?",
                            choices=["Hispanic or Latin", "Asian", "White", "Black or African American",
                                     "American Indian", "other / prefer not to answer"])
    party = models.CharField(initial=None,
                             verbose_name='In politics today, do you consider yourself a Republican, a Democrat , or an Independent?',
                             choices=['Republican', 'Democrat', 'Independent'], )
    favmovie = models.CharField(initial=None,
                                verbose_name="What is your favorite movie?")
    favtvshow = models.CharField(initial=None,
                                 verbose_name="What is your favorite TV show?")
    favbook = models.CharField(initial=None,
                               verbose_name="What is your favorite book?")
    favanimal = models.CharField(initial=None,
                                 verbose_name="What is your favorite animal?")
    purpose = models.LongStringField(initial=None,
                                     blank=True,
                                     verbose_name="Taking into account the following instruction, what do you think this experiment is about? Instruction: Please do not use the words 'Decision', and 'Study'.")
    attentioncheck = models.LongStringField(initial=None,
                                            blank=True,
                                            verbose_name="Based on the following sentence what is your favorite color? When asked for your favorite color, please answer: 'aliceblue'.")
    actsat = models.IntegerField(initial=None)
    sat = models.IntegerField(initial=None,
                              blank=True,
                              verbose_name='What was your highest SAT score?',
                              )
    act = models.IntegerField(initial=None,
                              blank=True,
                              verbose_name='What was your highest ACT score?',
                              )
    gpa_hs = models.FloatField(initial=None,
                               verbose_name='What is your final (or current) high school GPA?')
    gpa_college = models.FloatField(initial=None, blank=True,
                                    verbose_name='What is your final (or current) college GPA?')


# PAGES
class survey(Page):
    form_model = 'player'
    form_fields = ['birthday', 'gender', 'profession', 'fieldofstudy', 'occupation', 'nationality',
                   'education', 'race', 'state',
                   'religion', 'party', 'favmovie', 'favtvshow', 'favbook','favanimal',
                   'purpose', 'actsat', 'act', 'sat', 'gpa_college', 'gpa_hs',
                   'attentioncheck']


page_sequence = [survey]
