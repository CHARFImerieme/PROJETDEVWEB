# coding: utf-8

import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))
DB_FILE = os.path.join(BASEDIR, 'database.sqlite')

class Config:
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DB_FILE = DB_FILE
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{DB_FILE}'


class Production(Config):
    DEBUG = False


class Development(Config):
    ENV = "development"
    DEBUG = True


# Initial data to populate the DB with
class info:
    gastro = 'Gastronomie'
    cu = 'Culture'
    hist = 'Historique'
    act = 'Activités'

USERS = [
    {'name': 'Paris',
     'Info': [info.gastro, info.cu, info.hist, info.act],
     },
    {'name': 'Lyon',
     'Info': [info.gastro, info.cu, info.hist, info.act],
     },
    {'name': 'Marseilles',
     'Info': [info.gastro, info.cu, info.hist, info.act],
     },
    {'name': 'Bordeaux',
     'Info': [info.gastro, info.cu, info.hist, info.act],
     },
    {'name': 'Toulouse',
     'Info': [info.gastro, info.cu, info.hist, info.act],
     },
    {'name': 'Nice',
     'Info': [info.gastro, info.cu, info.hist, info.act],
     },
    {'name': 'Bretagne',
     'Info': [info.gastro, info.cu, info.hist, info.act],
     },
    {'name': 'Chamonix Mont Blanc',
     'Info': [info.gastro, info.cu, info.hist, info.act],
     },
    {'name': 'Strasbourg',
     'Info': [info.gastro, info.cu, info.hist, info.act],
     },
     {'name': 'Lille',
      'Info': [info.gastro, info.cu, info.hist, info.act],
      },
]

class WebDevException(Exception):
    pass


# VIM MODLINE
# vim: ai ts=4 sw=4 sts=4 expandtab fileencoding=utf8
