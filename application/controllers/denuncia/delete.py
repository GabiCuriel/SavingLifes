import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_denuncia, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(id_denuncia) # call GET_DELETE function
            elif privsession_privilegeilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_denuncia, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(id_denuncia) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(id_denuncia, **k):

    @staticmethod
    def POST_DELETE(id_denuncia, **k):
    '''

    def GET(self, id_denuncia, **k):
        message = None # Error message
        id_denuncia = config.check_secure_val(str(id_denuncia)) # HMAC id_denuncia validate
        result = config.model.get_denuncia(int(id_denuncia)) # search  id_denuncia
        result.id_denuncia = config.make_secure_val(str(result.id_denuncia)) # apply HMAC for id_denuncia
        return config.render.delete(result, message) # render delete.html with user data

    def POST(self, id_denuncia, **k):
        form = config.web.input() # get form data
        form['id_denuncia'] = config.check_secure_val(str(form['id_denuncia'])) # HMAC id_denuncia validate
        result = config.model.delete_denuncia(form['id_denuncia']) # get denuncia data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            id_denuncia = config.check_secure_val(str(id_denuncia))  # HMAC user validate
            id_denuncia = config.check_secure_val(str(id_denuncia))  # HMAC user validate
            result = config.model.get_denuncia(int(id_denuncia)) # get id_denuncia data
            result.id_denuncia = config.make_secure_val(str(result.id_denuncia)) # apply HMAC to id_denuncia
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/denuncia') # render denuncia delete.html 
