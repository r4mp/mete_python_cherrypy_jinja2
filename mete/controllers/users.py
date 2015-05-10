from controllers.basehandler import BaseHandler
from models.user import User

import json

import cherrypy
class Users(BaseHandler):

    #@cherrypy.expose
    def index(self, *vpath):
        print('vpath: ', vpath)
        users = User.list(cherrypy.request.db)

        #users[1].payment(cherrypy.request.db, 10)
        
        template = self.templateEnv.get_template('users/index.html')
        return template.render(users=users)

    #@cherrypy.expose
    def new(self, name = "", email = "", balance = 0):

        if cherrypy.request.method == 'GET':
            template = self.templateEnv.get_template('users/new.html')
            return template.render()
        elif cherrypy.request.method == 'POST':

            user = User()
            user.name = name
            user.email = email
            user.balance = balance

            cherrypy.request.db.add(user)
        else:
            pass

    def show(self, id = 0):
        print(id)

