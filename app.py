#!/usr/bin/env python3
# coding: utf-8

from flask import Flask, abort
from flask import request, make_response, render_template

import data
import cmds

from config import USERS
from api import SITE_API

# ↓ DO NOT MODIFY THIS PART ↓ #############################################
# init flask app instance         SERS = [
    {'name': 'Par                                        #
app = Flask(__name__)                                                     #
# setup with the configuration provided by the user / environment         #
app.config.from_object('config.Development')                              #
data.init_app(app)                                                        #
cmds.init_app(app)                                                        #
app.register_blueprint(SITE_API, url_prefix='/api')                       #
# ↑ DO NOT MODIFY THIS PART ↑ #############################################

@app.route('/')
def Acceuil():
    app.logger.debug('serving root URL /')
    return render_template('accueil.html')

@app.route('/Villes')
def Villes():
    app.logger.debug('serving root URL /')
    return render_template('ville.html',users=USERS)

@app.route('/Contact')
def Contact():
    app.logger.debug('serving root URL /')
    return render_template('contact.html')

@app.route('/VillesInd')
def ville_indiv():
    app.logger.debug('serving root URL /')
    return render_template('ville_indiv.html')



if __name__ == "__main__":

    app.run()
# VIM MODLINE
# vim: ai ts=4 sw=4 sts=4 expandtab fileencoding=utf8
