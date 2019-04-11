import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_desaparecidos, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(id_desaparecidos) # call GET_DELETE function
            elif privsession_privilegeilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_desaparecidos, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(id_desaparecidos) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(id_desaparecidos, **k):

    @staticmethod
    def POST_DELETE(id_desaparecidos, **k):
    '''

    def GET(self, id_desaparecidos, **k):
        message = None # Error message
        id_desaparecidos = config.check_secure_val(str(id_desaparecidos)) # HMAC id_desaparecidos validate
        result = config.model.get_desaparecidos(int(id_desaparecidos)) # search  id_desaparecidos
        result.id_desaparecidos = config.make_secure_val(str(result.id_desaparecidos)) # apply HMAC for id_desaparecidos
        return config.render.delete(result, message) # render delete.html with user data

    def POST(self, id_desaparecidos, **k):
        form = config.web.input() # get form data
        form['id_desaparecidos'] = config.check_secure_val(str(form['id_desaparecidos'])) # HMAC id_desaparecidos validate
        result = config.model.delete_desaparecidos(form['id_desaparecidos']) # get desaparecidos data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            id_desaparecidos = config.check_secure_val(str(id_desaparecidos))  # HMAC user validate
            id_desaparecidos = config.check_secure_val(str(id_desaparecidos))  # HMAC user validate
            result = config.model.get_desaparecidos(int(id_desaparecidos)) # get id_desaparecidos data
            result.id_desaparecidos = config.make_secure_val(str(result.id_desaparecidos)) # apply HMAC to id_desaparecidos
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/desaparecidos') # render desaparecidos delete.html 
