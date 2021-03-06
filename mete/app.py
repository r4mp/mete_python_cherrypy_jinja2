#/bin/python
# -*- coding: utf-8 -*-

__author__    = 'Gerrit Giehl <gerrit.giehl@email-versand.net>'
__contact__   = 'gerrit.giehl@email-versand.net'
__date__      = '09 Mai 2015'

from db import SAEnginePlugin, SATool
from controllers.basehandler import BaseHandler
from controllers.drinks import Drinks
from controllers.users import Users
from controllers.audits import Audits
import os.path

import cherrypy

APPDIR = os.path.dirname(os.path.abspath(__file__))
CONFIGFILE = os.path.join(APPDIR, 'server.conf')

def main():
    SAEnginePlugin(cherrypy.engine).subscribe()
    cherrypy.tools.db = SATool()

    d = cherrypy.dispatch.RoutesDispatcher()

    root = BaseHandler()
    d.connect('root', "/", controller=root, action='index')

    drinks = Drinks()
    d.connect('drinks', '/drinks', controller=drinks, action='index')
    d.connect('drinks_show', '/drinks/{id:([0-9]+)}', controller=drinks, action='show')
    d.connect('drinks_new', '/drinks/new', controller=drinks, action='new')
    d.connect('drinks_edit', '/drinks/{id:([0-9]+)}/edit', controller=drinks, action='edit')

    users = Users()
    d.connect('users', '/users', controller=users, action='index')
    d.connect('users_show', '/users/{id:([0-9]+)}', controller=users, action='show')
    d.connect('users_new', '/users/new', controller=users, action='new')
    d.connect('users_stats', '/users/stats', controller=users, action='stats')
    d.connect('users_edit', '/users/{id:([0-9]+)}/edit', controller=users, action='edit')
    d.connect('users_delete', '/users/{id:([0-9]+)}/delete', controller=users, action='delete')
    d.connect('users_payment', '/users/{id:([0-9]+)}/payment', controller=users, action='payment')
    d.connect('users_deposit', '/users/{id:([0-9]+)}/deposit', controller=users, action='deposit')

    audits = Audits()
    d.connect('audits', '/audits', controller=audits, action='index')

    confdict = {'/': {'request.dispatch': d}}
    
    cherrypy.config.update(CONFIGFILE)
    cherrypy.config.update(confdict)

    #cherrypy.quickstart(None, config = CONFIGFILE)
    app = cherrypy.tree.mount(root = None, config = CONFIGFILE)
    app.merge(confdict)

    cherrypy.engine.start()
    cherrypy.engine.block()

if __name__ == "__main__":
    main()
