import config
import hashlib
import app
import os
import shutil

class Insert:

    def __init__(self):
        pass

    '''
    def GET(self):
        if app.session.loggedin is True:
            # session_username = app.session.username
            session_username = app.session.privilege  # get the session_privilege
            if session_username == 0: # admin user
                return self.GET_INSERT() # call GET_INSERT() function
            elif session_username == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_username = app.session.privilege # get the session_privilege
            if session_username == 0: # admin user
                return self.POST_INSERT() # call POST_EDIT function
            elif privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_INSERT():

    @staticmethod
    def POST_INSERT():
    '''

    def GET(self):
        return config.render.insert() # render insert.html

    def POST(self):
        form = config.web.input() # get form data
        x = config.web.input(imagen={})
        filedir = 'static/files/usuarios_img'
        filepath=x.imagen.filename.replace('\\','/')
        filename=filepath.split('/')[-1]
        with open(os.path.join(filedir, filename), 'wb') as f:
            shutil.copyfileobj(x.imagen.file, f)
        imagen = filename

        # call model insert_usuarios and try to insert new data
        config.model.insert_usuarios(
            form['nombre_u'],
            form['email_u'],
            form['telefono_u'],
            form['password'],
            form['municipio_u'],
            form['colonia_u'],
            form['tipo_u'],
            imagen,
        )
        raise config.web.seeother('/usuarios') # render usuarios index.html
