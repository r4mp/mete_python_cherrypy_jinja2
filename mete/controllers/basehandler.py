from jinja2 import Environment, FileSystemLoader
import os.path
import cherrypy

class BaseHandler(object):

    #templateLoader = FileSystemLoader(searchpath="templates/")
    templateLoader = FileSystemLoader(searchpath=os.path.join(os.path.dirname(__file__), "../templates/"))
    templateEnv = Environment(loader=templateLoader)

    #@cherrypy.expose
    def index(self):
        template = self.templateEnv.get_template('login.html')
        return template.render()

    def get_current_user(self):
        return self.get_secure_cookie("user")
