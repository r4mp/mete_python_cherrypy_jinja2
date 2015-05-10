from controllers.basehandler import BaseHandler
from models.drink import Drink

import json

import cherrypy
class Drinks(BaseHandler):

    #@cherrypy.expose
    def index(self):
        drinks = Drink.list(cherrypy.request.db)

        template = self.templateEnv.get_template('drinks/index.html')
        return template.render(drinks=drinks)

    #@cherrypy.expose(alias="new.json")
    #@cherrypy.tools.json_out()
    #def new_json(self):
    #    return [ drink.to_JSON() for drink in Drink.list(cherrypy.request.db) ]

    #@cherrypy.expose
    def new(self, name = "", price = 0, bottle_size = 0, caffeine = 0, logo_url = ""):

        if cherrypy.request.method == 'GET':
            template = self.templateEnv.get_template('drinks/new.html')
            return template.render(drinks=[])
        elif cherrypy.request.method == 'POST':

            drink = Drink()
            drink.name = name
            drink.price = price
            drink.bottle_size = bottle_size
            drink.caffeine = caffeine
            drink.logo_url = logo_url

            cherrypy.request.db.add(drink)
        else:
            pass


