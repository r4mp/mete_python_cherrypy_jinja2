from controllers.basehandler import BaseHandler
import tornado

class MainHandler(BaseHandler):
    
    def get(self):
        template = self.templateEnv.get_template('login.html')
        self.write(template.render())


