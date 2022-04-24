#!/usr/bin/env python3
# coding: utf-8

from flask import Flask, abort
from flask import request, make_response, render_template

from config import users
import config
from api import SITE_API

# ↓ DO NOT MODIFY THIS PART ↓ #############################################
# init flask app instance                                                 #
app = Flask(__name__)                                                     #
# setup with the configuration provided by the user / environment         #
app.config.from_object('config.Development')                              #                                                    #
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
    return render_template('ville.html',users=users)

@app.route('/Contact')
def Contact():
    app.logger.debug('serving root URL /')
    return render_template('contact.html')


@app.route('/Paris')
def Paris():
    app.logger.debug('serving root URL /')
    return render_template('Paris.html')

@app.route('/Bordeaux')
def Bordeaux():
    app.logger.debug('serving root URL /')
    return render_template('Bordeaux.html')

@app.route('/Lille')
def Lille():
    app.logger.debug('serving root URL /')
    return render_template('Lille.html')

@app.route('/ChamonixMontBlanc')
def ChamonixMontBlanc():
    app.logger.debug('serving root URL /')
    return render_template('Chamonix Mont Blanc.html')

@app.route('/Lyon')
def Lyon():
    app.logger.debug('serving root URL /')
    return render_template('Lyon.html')

@app.route('/Marseille')
def Marseille():
    app.logger.debug('serving root URL /')
    return render_template('Marseille.html')

@app.route('/Nice')
def Nice():
    app.logger.debug('serving root URL /')
    return render_template('Nice.html')

@app.route('/Strasbourg')
def Strasbourg():
    app.logger.debug('serving root URL /')
    return render_template('Strasbourg.html')

@app.route('/Toulouse')
def Toulouse():
    app.logger.debug('serving root URL /')
    return render_template('Toulouse.html')

@app.route('/SaintMalo')
def SaintMalo():
    app.logger.debug('serving root URL /')
    return render_template('Saint Malo.html')

@app.route('/ville/<user>')
def profile(user):
    ville=user+'.html'
    app.logger.debug(ville)
    return render_template(ville,users=users)

def search(request):
    app.logger.debug(request.args)
    pattern=request.args.get('pattern')
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
