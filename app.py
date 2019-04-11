import web
import config

ssl = False

urls = (
    '/', 'application.controllers.main.index.Index',
    '/login', 'application.controllers.main.login.Login',
    '/logout', 'application.controllers.main.logout.Logout',
    '/users', 'application.controllers.users.index.Index',
    '/users/printer', 'application.controllers.users.printer.Printer',
    '/users/view/(.+)', 'application.controllers.users.view.View',
    '/users/edit/(.+)', 'application.controllers.users.edit.Edit',
    '/users/delete/(.+)', 'application.controllers.users.delete.Delete',
    '/users/insert', 'application.controllers.users.insert.Insert',
    '/users/change_pwd', 'application.controllers.users.change_pwd.Change_pwd',
    '/logs', 'application.controllers.logs.index.Index',
    '/logs/printer', 'application.controllers.logs.printer.Printer',
    '/logs/view/(.+)', 'application.controllers.logs.view.View',
    '/adoptar', 'application.controllers.adoptar.index.Index',
    '/adoptar/view/(.+)', 'application.controllers.adoptar.view.View',
    '/adoptar/edit/(.+)', 'application.controllers.adoptar.edit.Edit',
    '/adoptar/delete/(.+)', 'application.controllers.adoptar.delete.Delete',
    '/adoptar/insert', 'application.controllers.adoptar.insert.Insert',
    '/comentarios', 'application.controllers.comentarios.index.Index',
    '/comentarios/view/(.+)', 'application.controllers.comentarios.view.View',
    '/comentarios/edit/(.+)', 'application.controllers.comentarios.edit.Edit',
    '/comentarios/delete/(.+)', 'application.controllers.comentarios.delete.Delete',
    '/comentarios/insert', 'application.controllers.comentarios.insert.Insert',
    '/desaparecidos', 'application.controllers.desaparecidos.index.Index',
    '/desaparecidos/view/(.+)', 'application.controllers.desaparecidos.view.View',
    '/desaparecidos/edit/(.+)', 'application.controllers.desaparecidos.edit.Edit',
    '/desaparecidos/delete/(.+)', 'application.controllers.desaparecidos.delete.Delete',
    '/desaparecidos/insert', 'application.controllers.desaparecidos.insert.Insert',
    '/usuarios', 'application.controllers.usuarios.index.Index',
    '/usuarios/view/(.+)', 'application.controllers.usuarios.view.View',
    '/usuarios/edit/(.+)', 'application.controllers.usuarios.edit.Edit',
    '/usuarios/delete/(.+)', 'application.controllers.usuarios.delete.Delete',
    '/usuarios/insert', 'application.controllers.usuarios.insert.Insert',
    '/denuncia', 'application.controllers.denuncia.index.Index',
    '/denuncia/view/(.+)', 'application.controllers.denuncia.view.View',
    '/denuncia/edit/(.+)', 'application.controllers.denuncia.edit.Edit',
    '/denuncia/delete/(.+)', 'application.controllers.denuncia.delete.Delete',
    '/denuncia/insert', 'application.controllers.denuncia.insert.Insert',
    
    '/api_adoptar/?', 'application.api.adoptar.api_adoptar.Api_adoptar',
    '/api_comentarios/?', 'application.api.comentarios.api_comentarios.Api_comentarios',
    '/api_denuncia/?', 'application.api.denuncia.api_denuncia.Api_denuncia',
   '/api_desaparecidos/?', 'application.api.desaparecidos.api_desaparecidos.Api_desaparecidos',
    '/api_usuarios/?', 'application.api.usuarios.api_usuarios.Api_usuarios',
    '/api_users/?', 'application.api.users.api_users.Api_users',
    #'/api_table_name/?', 'application.api.table_name.api_table_name.Api_table_name',
)

app = web.application(urls, globals())

if ssl is True:
    from web.wsgiserver import CherryPyWSGIServer
    CherryPyWSGIServer.ssl_certificate = "ssl/server.crt"
    CherryPyWSGIServer.ssl_private_key = "ssl/server.key"

if web.config.get('_session') is None:
    db = config.db
    store = web.session.DBStore(db, 'sessions')
    session = web.session.Session(
        app,
        store,
        initializer={
        'login': 0,
        'privilege': -1,
        'user': 'anonymous',
        'loggedin': False,
        'count': 0
        }
        )
    web.config._session = session
    web.config.session_parameters['cookie_name'] = 'kuorra'
    web.config.session_parameters['timeout'] = 10
    web.config.session_parameters['expired_message'] = 'Session expired'
    web.config.session_parameters['ignore_expiry'] = False
    web.config.session_parameters['ignore_change_ip'] = False
    web.config.session_parameters['secret_key'] = 'fLjUfxqXtfNoIldA0A0J'
else:
    session = web.config._session


class Count:
    def GET(self):
        session.count += 1
        return str(session.count)


def InternalError(): 
    raise config.web.seeother('/')


def NotFound():
    raise config.web.seeother('/')

if __name__ == "__main__":
    db.printing = False # hide db transactions
    web.config.debug = False # hide debug print
    web.config.db_printing = False # hide db transactions
    app.internalerror = InternalError
    app.notfound = NotFound
    app.run()
