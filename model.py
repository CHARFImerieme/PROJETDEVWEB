# coding: utf-8
# DOC:
# * association_proxy
#   https://docs.sqlalchemy.org/en/14/orm/extensions/associationproxy.html#simplifying-scalar-collections

from dataclasses import dataclass
from datetime import datetime
from typing import List

from sqlalchemy.ext.associationproxy import association_proxy

from config import WebDevException
from data import db


user_fields_table = db.Table('user_fields', db.metadata,
                             db.Column('field_id', db.Integer, db.ForeignKey(
                                 'field.id'), primary_key=True),
                             db.Column('user_id', db.Integer, db.ForeignKey(
                                 'user.id'), primary_key=True)
                             )

@dataclass
class User(db.Model):
    __tablename__ = 'user'
    id: int
    name: str
    birthday: datetime
    wikiid: int
    fds: List[str]
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    birthday = db.Column(db.DateTime, nullable=False)
    wikiid = db.Column(db.Integer, nullable=True)
    fds = db.relationship('Field', secondary=user_fields_table,
                          lazy='subquery',
                          backref=db.backref('users', lazy=True))

    def __str__(self):
        return self.name

    def __repr__(self):
        return (f'User(name={self.name}, birthday={self.birthday:%Y-%m-%d}, '
                f'fields={self.fields}, id={self.id})')

    fields = association_proxy('fds', 'name')

    @property
    def flat(self):
        user = {}
        for key in self.__table__.columns.keys():
            user.update({key:getattr(self, key)})
            user.update({'id': self.id})
        user.update({'fields':', '.join(getattr(self, 'fields'))})
        return user

@dataclass
class Field(db.Model):
    __tablename__ = 'field'
    id: int
    id = db.Column(db.Integer, primary_key=True)
    name: str
    name = db.Column(db.String(50), nullable=False, unique=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Field(name="{self.name}")'

    def __str__(self):
        return self.name


# TOOLS
USER_KEYS = {'name': str, 'birthday': datetime, 'fields': list, 'wikiid': int}


def add_user(user):
    """Add a user to the database, returns the user's id.
    "user" parameter is a dictionary with the following values:
        'name' and 'birthday' are mandatory.
        'fields' can be an empty list.
        'birthday' is a datetime object.

    >>> date = datetime.datetime.fromisoformat('1970-01-01')
    >>> user = {'name': 'Foo Bar', 'fields': ['baz', 'foz'],
                'birthday': date}
    >>> user_id = add_user(user)
    """
    if 'wikiid' not in user:  # Make tests pass anyway with no wikiid
        user.update({'wikiid': -1})
    # control user have all required fields
    provided_keys = user.keys()
    if len(provided_keys) > len(USER_KEYS.keys()):
        raise WebDevException('Too many values calling add_user, expecting %s' %
                              list(USER_KEYS.keys()))
    if provided_keys != USER_KEYS.keys():
        raise WebDevException('Missing value calling add_user, expecting %s' %
                              list(USER_KEYS.keys()))
    for k, ty in USER_KEYS.items():
        if type(user.get(k)) is not ty:
            raise ValueError(f'Wrong type for {k}, expecting {ty}')
    if user['wikiid'] == -1:
        user.pop('wikiid')
    # Extract fields to intanciate model.User
    fields = user.pop('fields')
    db.session.commit()
    # Add user record
    u = User(**user)
    # Restore user fieds
    user.update({'fields': fields})
    _update_user_fields(u, fields)
    db.session.add(u)
    db.session.commit()
    return u.id


def update_user(user):
    """Update a user already in DB.
    "user" parameter is a dictionary with at least the user's id to update and
    one or more values to update.
        'name', 'birthday' or 'fields'.
        'fields' is a list os strings.
        'birthday' is a datetime object.

    >>> # update fields for user with id 42 (adds 'boo' to fields)
    >>> user = {'id': 42, 'fields': ['boo']}
    >>> user_id = update_user(user)
    """
    if 'id' not in user:
        raise WebDevException('Need the user\'s id, got %s'
                              % list(user.keys()))
    # Test user with no value for USER_KEYS.keys()
    if not set(USER_KEYS.keys()) & set(user.keys()):
        raise WebDevException('Need at least one of: %s'
                              % list(USER_KEYS.keys()))
    # Is user really there
    if not User.query.get(user.get('id')):
        raise WebDevException('User not found: %s' % user)
    # Copy user to prevent modification on 'user'
    uu = dict(user)
    user_id = uu.pop('id')
    fields = uu.pop('fields', [])
    if uu:  # updates user only if 'name' or 'birthday' are present
        User.query.filter(User.id == user_id).update(uu)
    _update_user_fields(User.query.get(user_id), fields)
    db.session.commit()


def delete_user(user):
    """Remove a user from database
    "user" parameter is a dictionary with at least an 'id' value.
    >>> user = {'name': 'Foo Bar', 'id': 42}
    >>> delete_user(user)
    """
    if 'id' not in user:
        raise WebDevException('Need the user\'s id, got %s'
                              % list(user.keys()))
    # Is user really there
    to_del = User.query.get(user.get('id'))
    if not to_del:
        raise WebDevException('User not found: %s' % user)
    db.session.delete(to_del)
    db.session.commit()


def _update_user_fields(u, fds):
    """Update User.fields
    Create a new Field if needed"""
    for field in fds:
        f = Field.query.filter_by(name=field).one_or_none()
        if f is None:  # Create new Field
            u.fields.append(field)
        else:  # Use existing one
            u.fds.append(f)


# VIM MODLINE
# vim: ai ts=4 sw=4 sts=4 expandtab fileencoding=utf8
