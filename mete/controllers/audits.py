from controllers.basehandler import BaseHandler
from models.audit import Audit

import json

import cherrypy
class Audits(BaseHandler):

    def index(self):
        audits = Audit.list(cherrypy.request.db)

        template = self.templateEnv.get_template('audits/index.html')
        return template.render(audits=audits)

