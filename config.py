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
     'fields': [info.gastro, info.cu, info.hist, info.act],
     },
    {'name': 'Marseilles',
     'fields': [info.gastro, info.cu, info.hist, info.act],
     },
    {'name': 'Bordeaux',
     'fields': [info.gastro, info.cu, info.hist, info.act],
     },
    {'name': 'Toulouse',
     'fields': [info.gastro, info.cu, info.hist, info.act],
     },
    {'name': 'Nice',
     'fields': [info.gastro, info.cu, info.hist, info.act],
     },
    {'name': 'Bretagne',
     'fields': [info.gastro, info.cu, info.hist, info.act],
     },
    {'name': 'Chamonix Mont Blanc',
     'fields': [info.gastro, info.cu, info.hist, info.act],
     },
    {'name': 'Strasbourg',
     'fields': [info.gastro, info.cu, info.hist, info.act],
     },
     {'name': 'Lille',
      'fields': [info.gastro, info.cu, info.hist, info.act],
      },
]

class WebDevException(Exception):
    pass


# VIM MODLINE
# vim: ai ts=4 sw=4 sts=4 expandtab fileencoding=utf8
