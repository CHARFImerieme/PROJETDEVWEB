# coding: utf-8

import os

from datetime import datetime

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
class Fields:
    bio = 'biology'
    it = 'information science'
    logic = 'logic'
    math = 'mathematics'
    physics = 'physics'


USERS = [
    {'name': 'Katherine Johnson',
     'birthday': datetime.fromisoformat('1918-08-26'),
     'fields': [Fields.math, Fields.physics], 'wikiid': 25568315,
     },
    {'name': 'Alan Turing',
     'birthday': datetime.fromisoformat('1912-06-23'),
     'fields': [Fields.math, Fields.it], 'wikiid': 1208,
     },
    {'name': 'Kurt Gödel',
     'birthday': datetime.fromisoformat('1906-04-28'),
     'fields': [Fields.logic, Fields.math], 'wikiid': 16636,
     },
    {'name': 'John Neumann',
     'birthday': datetime.fromisoformat('1903-12-28'),
     'fields': [Fields.math, Fields.it], 'wikiid': 15942,
     },
    {'name': 'Alexander Grothendieck',
     'birthday': datetime.fromisoformat('1928-03-28'),
     'fields': [Fields.math], 'wikiid': 2042,
     },
    {'name': 'Marie Skłodowska-Curie',
     'birthday': datetime.fromisoformat('1867-11-07'),
     'fields': [Fields.physics], 'wikiid': 20408,
     },
    {'name': 'Hedy Lamarr',
     'birthday': datetime.fromisoformat('1914-01-01'),
     'fields': [Fields.it, Fields.math], 'wikiid': 170982,
     },
    {'name': 'Rachel Louise Carson',
     'birthday': datetime.fromisoformat('1947-05-27'),
     'fields': [Fields.bio], 'wikiid': 000000,
     },
    {'name': 'Maud Leonora Menten',
     'birthday': datetime.fromisoformat('1879-03-20'),
     'fields': [Fields.bio], 'wikiid': 000000,
     },
]


class WebDevException(Exception):
    pass


# VIM MODLINE
# vim: ai ts=4 sw=4 sts=4 expandtab fileencoding=utf8
