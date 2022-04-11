#!/usr/bin/env python3
# coding: utf-8

from flask import Flask, abort
from flask import request, make_response, render_template

import data
import cmds

from config import USERS
from api import SITE_API

# ↓ DO NOT MODIFY THIS PART ↓ #############################################
# init flask app instance                                                 #
app = Flask(__name__)                                                     #
# setup with the configuration provided by the user / environment         #
app.config.from_object('config.Development')                              #
data.init_app(app)                                                        #
cmds.init_app(app)                                                        #
app.register_blueprint(SITE_API, url_prefix='/api')                       #
# ↑ DO NOT MODIFY THIS PART ↑ #############################################

@app.route('/')
def Accueil():
    app.logger.debug('serving root URL /')
    return render_template('accueil.html')

@app.route('/Villes')
def Villes():
    app.logger.debug('serving users URL /users/')
    # The request contains an arguments in the query string
    if request.args:
        if search(request) !=0:
            return render_template('ville.html', users=search(request))
        else:
            return make_response('No result found',400)
    return render_template('ville.html',users=USERS)

@app.route('/Contact')
def Contact():
    app.logger.debug('serving root URL /')
    return render_template('contact.html')

@app.route('/VillesInd')
def ville_indiv():
    app.logger.debug('serving root URL /')
    return render_template('ville_indiv.html')

def search(request):
    app.logger.debug(request.args)
    pattern=request.args.get('pattern')
    users=USERS
    found_user = []
    for user in users :
        if pattern.upper() in user['name'].upper():
            found_user.append(user)
    if not found_user:
        found_user = 0
    return found_user


if __name__ == "__main__":

    app.run()
# VIM MODLINE
# vim: ai ts=4 sw=4 sts=4 expandtab fileencoding=utf8
