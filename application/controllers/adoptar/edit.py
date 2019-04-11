import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_publicar, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(id_publicar) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_publicar, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(id_publicar) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_EDIT(id_publicar, **k):

    @staticmethod
    def POST_EDIT(id_publicar, **k):
        
    '''

    def GET(self, id_publicar, **k):
        message = None # Error message
        id_publicar = config.check_secure_val(str(id_publicar)) # HMAC id_publicar validate
        result = config.model.get_adoptar(int(id_publicar)) # search for the id_publicar
        result.id_publicar = config.make_secure_val(str(result.id_publicar)) # apply HMAC for id_publicar
        return config.render.edit(result, message) # render adoptar edit.html

    def POST(self, id_publicar, **k):
        form = config.web.input()  # get form data
        form['id_publicar'] = config.check_secure_val(str(form['id_publicar'])) # HMAC id_publicar validate
        # edit user with new data
        result = config.model.edit_adoptar(
            form['id_publicar'],
            form['nom_persona'],
            form['email'],
            form['telefono'],
            form['municipio'],
            form['colonia'],
            form['fecha'],
            form['nom_mascota'],
            form['edad_mascota'],
            form['sexo_mascota'],
            form['tipo_mascota'],
            form['descripcion_mascota'],
            form['id_usuario'],
        )
        if result == None: # Error on udpate data
            id_publicar = config.check_secure_val(str(id_publicar)) # validate HMAC id_publicar
            result = config.model.get_adoptar(int(id_publicar)) # search for id_publicar data
            result.id_publicar = config.make_secure_val(str(result.id_publicar)) # apply HMAC to id_publicar
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/adoptar') # render adoptar index.html
