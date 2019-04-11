import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_desaparecidos, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(id_desaparecidos) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_desaparecidos, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(id_desaparecidos) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_EDIT(id_desaparecidos, **k):

    @staticmethod
    def POST_EDIT(id_desaparecidos, **k):
        
    '''

    def GET(self, id_desaparecidos, **k):
        message = None # Error message
        id_desaparecidos = config.check_secure_val(str(id_desaparecidos)) # HMAC id_desaparecidos validate
        result = config.model.get_desaparecidos(int(id_desaparecidos)) # search for the id_desaparecidos
        result.id_desaparecidos = config.make_secure_val(str(result.id_desaparecidos)) # apply HMAC for id_desaparecidos
        return config.render.edit(result, message) # render desaparecidos edit.html

    def POST(self, id_desaparecidos, **k):
        form = config.web.input()  # get form data
        form['id_desaparecidos'] = config.check_secure_val(str(form['id_desaparecidos'])) # HMAC id_desaparecidos validate
        # edit user with new data
        result = config.model.edit_desaparecidos(
            form['id_desaparecidos'],
            form['nombre_p'],
            form['email_p'],
            form['telefono_p'],
            form['municipio_p'],
            form['colonia_p'],
            form['fecha_p'],
            form['nombre_m'],
            form['edad_m'],
            form['sexo_m'],
            form['tipo_m'],
            form['descripcion_m'],
            form['id_usuario'],
        )
        if result == None: # Error on udpate data
            id_desaparecidos = config.check_secure_val(str(id_desaparecidos)) # validate HMAC id_desaparecidos
            result = config.model.get_desaparecidos(int(id_desaparecidos)) # search for id_desaparecidos data
            result.id_desaparecidos = config.make_secure_val(str(result.id_desaparecidos)) # apply HMAC to id_desaparecidos
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/desaparecidos') # render desaparecidos index.html
