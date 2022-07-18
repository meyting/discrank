from os import environ

SESSION_CONFIGS = [
    dict(
        name='welcome',
        display_name='welcome',
        num_demo_participants=20,
        app_sequence=['welcome'],
    ),
    dict(
        name='beliefs',
        display_name='beliefs',
        num_demo_participants=20,
        app_sequence=['beliefs'],
    ),
    dict(
        name='rank',
        display_name='rank',
        num_demo_participants=20,
        app_sequence=['rank'],
        version='old',
    ),
    dict(
        name='rank_with_refresh',
        display_name='rank with refresh',
        num_demo_participants=20,
        app_sequence=['rank'],
        version='new',
    ),
    dict(
        name='survey',
        display_name='survey',
        num_demo_participants=20,
        app_sequence=['survey'],
    ),
    dict(
        name='all_realeffort',
        display_name='all (realeffort)',
        num_demo_participants=20,
        app_sequence=['welcome', 'beliefs', 'rank', 'survey'],
        task='realeffort',
    ),
    dict(
        name='all_logic',
        display_name='all (logic)',
        num_demo_participants=20,
        app_sequence=['welcome','beliefs', 'rank', 'survey'],
        task="logic",
    ),
    dict(
        name='all',
        display_name='all',
        num_demo_participants=20,
        app_sequence=['welcome','beliefs', 'rank', 'survey'],
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=5.00, doc=""
)

PARTICIPANT_FIELDS = ["task"]
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = False

AUTH_LEVEL = 'STUDY' # wieder löschen wenn Umgebungsvariable gesetzt			!!!!!!!!!!!!!!!


ADMIN_USERNAME = 'discrank'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = 'discrank'

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '1494696161603'
