# coding: utf-8

import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))
#DB_FILE = os.path.join(BASEDIR, 'database.sqlite')

class Config:
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #DB_FILE = DB_FILE
    #SQLALCHEMY_DATABASE_URI = f'sqlite:///{DB_FILE}'


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
    {'name':'Paris',
    'photo': 'images_templates/Paris.jpg',
     'Info': [info.gastro, info.cu, info.hist, info.act],
     },
    {'name':'Lyon',
    'photo': 'images_templates/Lyon.jpg',
     'Info': [info.gastro, info.cu, info.hist, info.act],
     },
    {'name':'Marseille',
    'photo': 'images_templates/Marseille.jpg',
     'Info': [info.gastro, info.cu, info.hist, info.act],
     },
    {'name':'Bordeaux',
     'photo': 'images_templates/Bordeaux.jpg',
     'Info': [info.gastro, info.cu, info.hist, info.act],
     },
    {'name': 'Toulouse',
    'photo': 'images_templates/Toulouse.jpg',
     'Info': [info.gastro, info.cu,info.hist, info.act],
     },
    {'name':'Nice',
    'photo': 'images_templates/Nice.jpg',
     'Info': [info.gastro, info.cu, info.hist, info.act],
     },
    {'name':'Saint Malo',
    'photo': 'images_templates/Saint Malo.jpg',
     'Info': [info.gastro, info.cu, info.hist, info.act],
     },
    {'name':'Chamonix Mont Blanc',
    'photo': 'images_templates/Chamonix Mont Blanc.jpg',
     'Info': [info.gastro, info.cu, info.hist, info.act],
     },
    {'name':'Strasbourg',
    'photo': 'images_templates/Strasbourg.jpg',
     'Info': [info.gastro, info.cu, info.hist, info.act],
     },
     {'name':'Lille',
     'photo': 'images_templates/Lille.jpg',
      'Info': [info.gastro, info.cu, info.hist, info.act],
      },
]

class WebDevException(Exception):
    pass


# VIM MODLINE
# vim: ai ts=4 sw=4 sts=4 expandtab fileencoding=utf8
