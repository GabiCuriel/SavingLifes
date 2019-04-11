import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_publicar, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(id_publicar) # call GET_DELETE function
            elif privsession_privilegeilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_publicar, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(id_publicar) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(id_publicar, **k):

    @staticmethod
    def POST_DELETE(id_publicar, **k):
    '''

    def GET(self, id_publicar, **k):
        message = None # Error message
        id_publicar = config.check_secure_val(str(id_publicar)) # HMAC id_publicar validate
        result = config.model.get_adoptar(int(id_publicar)) # search  id_publicar
        result.id_publicar = config.make_secure_val(str(result.id_publicar)) # apply HMAC for id_publicar
        return config.render.delete(result, message) # render delete.html with user data

    def POST(self, id_publicar, **k):
        form = config.web.input() # get form data
        form['id_publicar'] = config.check_secure_val(str(form['id_publicar'])) # HMAC id_publicar validate
        result = config.model.delete_adoptar(form['id_publicar']) # get adoptar data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            id_publicar = config.check_secure_val(str(id_publicar))  # HMAC user validate
            id_publicar = config.check_secure_val(str(id_publicar))  # HMAC user validate
            result = config.model.get_adoptar(int(id_publicar)) # get id_publicar data
            result.id_publicar = config.make_secure_val(str(result.id_publicar)) # apply HMAC to id_publicar
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/adoptar') # render adoptar delete.html 
