# coding: utf-8

from flask import request, abort, current_app
from flask import Blueprint, jsonify

SITE_API = Blueprint('api', __name__,)


@SITE_API.route('/')
@SITE_API.route('/<string:node0>', methods=['GET', 'POST'])
def api(node0=None):
    current_app.logger.debug('Looking at "{}" resource'.format(node0))
    abort(501)


# VIM MODLINE
# vim: ai ts=4 sw=4 sts=4 expandtab fileencoding=utf8
