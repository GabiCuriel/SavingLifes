import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_denuncia, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(id_denuncia) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_denuncia, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(id_denuncia) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_EDIT(id_denuncia, **k):

    @staticmethod
    def POST_EDIT(id_denuncia, **k):
        
    '''

    def GET(self, id_denuncia, **k):
        message = None # Error message
        id_denuncia = config.check_secure_val(str(id_denuncia)) # HMAC id_denuncia validate
        result = config.model.get_denuncia(int(id_denuncia)) # search for the id_denuncia
        result.id_denuncia = config.make_secure_val(str(result.id_denuncia)) # apply HMAC for id_denuncia
        return config.render.edit(result, message) # render denuncia edit.html

    def POST(self, id_denuncia, **k):
        form = config.web.input()  # get form data
        form['id_denuncia'] = config.check_secure_val(str(form['id_denuncia'])) # HMAC id_denuncia validate
        # edit user with new data
        result = config.model.edit_denuncia(
            form['id_denuncia'],
            form['nombre_d'],
            form['descripcion_d'],
            form['municipio_d'],
            form['colonia_d'],
        )
        if result == None: # Error on udpate data
            id_denuncia = config.check_secure_val(str(id_denuncia)) # validate HMAC id_denuncia
            result = config.model.get_denuncia(int(id_denuncia)) # search for id_denuncia data
            result.id_denuncia = config.make_secure_val(str(result.id_denuncia)) # apply HMAC to id_denuncia
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/denuncia') # render denuncia index.html
