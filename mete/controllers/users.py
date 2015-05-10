from controllers.basehandler import BaseHandler
from models.user import User
from models.drink import Drink

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
            template = self.templateEnv.get_template('users/form.html')
            return template.render(user=[], link='/users/new', button_value='New User', header='Welcome, fellow hacker <small>join the party!</small>')
        elif cherrypy.request.method == 'POST':

            user = User()
            user.name = name
            user.email = email

            if balance.isdigit():
                user.balance = int(float(balance) * 100)
            else:
                user.balance = 0

            cherrypy.request.db.add(user)
            cherrypy.request.db.flush()

            raise cherrypy.HTTPRedirect('/users/' + str(user.id))
        else:
            pass

    def show(self, id = 0):
        user = User.get(cherrypy.request.db, int(id))

        if not hasattr(user, 'id'):
            return

        drinks = Drink.list(cherrypy.request.db)
        
        template = self.templateEnv.get_template('users/show.html')
        return template.render(user=user, drinks=drinks)

    def delete(self, id = 0):
            User.delete(cherrypy.request.db, int(id))
            raise cherrypy.HTTPRedirect('/users')

    def stats(self):
        users_count = User.count(cherrypy.request.db)
        users_balance_sum = User.balance_sum(cherrypy.request.db)
        template = self.templateEnv.get_template('users/stats.html')
        return template.render(users_count=users_count, users_balance_sum=users_balance_sum)

    def deposit(self, id = 0, amount = 0):
        User.deposit(cherrypy.request.db, int(id), int(amount))
        raise cherrypy.HTTPRedirect('/users/' + str(int(id)))

    def payment(self, id = 0, amount = 0):
        User.payment(cherrypy.request.db, int(id), int(amount))
        raise cherrypy.HTTPRedirect('/users/' + str(int(id)))
