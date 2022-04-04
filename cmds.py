# coding: utf-8
import os

from data import db
from config import USERS
from model import User
from model import add_user


def create_db():
    """Creates database"""
    db.create_all()


def drop_db():
    """Cleans database"""
    db.drop_all()


def show_db():
    """Show db content"""
    print(User.query.all())


def reset_db():
    """Remove, re-create and re-populate database"""
    db_file = db.get_app().config.get('DB_FILE')
    try:
        os.unlink(db_file)
        print(f'Removed {db_file}')
    except FileNotFoundError:
        print(f'Warning, db not found: "{db_file}"')
    create_db()
    populate_db()


def populate_db():
    """Populate database with config.USERS content"""
    for user in USERS:  # Create users
        add_user(user)


def init_app(app):
    # add multiple commands in a bulk
    for command in [create_db, drop_db, populate_db, show_db, reset_db]:
        app.cli.add_command(app.cli.command()(command))

# VIM MODLINE
# vim: ai ts=4 sw=4 sts=4 expandtab fileencoding=utf8
