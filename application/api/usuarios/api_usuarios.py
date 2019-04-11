import web
import config
import json


class Api_usuarios:
    def get(self, id_usuario):
        try:
            # http://0.0.0.0:8080/api_usuarios?user_hash=12345&action=get
            if id_usuario is None:
                result = config.model.get_all_usuarios()
                usuarios_json = []
                for row in result:
                    tmp = dict(row)
                    usuarios_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(usuarios_json)
            else:
                # http://0.0.0.0:8080/api_usuarios?user_hash=12345&action=get&id_usuario=1
                result = config.model.get_usuarios(int(id_usuario))
                usuarios_json = []
                usuarios_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(usuarios_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            usuarios_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(usuarios_json)

# http://0.0.0.0:8080/api_usuarios?user_hash=12345&action=put&id_usuario=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=0
    def put(self, nombre_u,email_u,telefono_u,password,municipio_u,colonia_u,tipo_u,imagen):
        try:
            config.model.insert_usuarios(nombre_u,email_u,telefono_u,password,municipio_u,colonia_u,tipo_u,imagen)
            usuarios_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(usuarios_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_usuarios?user_hash=12345&action=delete&id_usuario=1
    def delete(self, id_usuario):
        try:
            config.model.delete_usuarios(id_usuario)
            usuarios_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(usuarios_json)
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_usuarios?user_hash=12345&action=update&id_usuario=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=default.jpg
    def update(self, id_usuario, nombre_u,email_u,telefono_u,password,municipio_u,colonia_u,tipo_u,imagen):
        try:
            config.model.edit_usuarios(id_usuario,nombre_u,email_u,telefono_u,password,municipio_u,colonia_u,tipo_u,imagen)
            usuarios_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(usuarios_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            usuarios_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(usuarios_json)

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            id_usuario=None,
            nombre_u=None,
            email_u=None,
            telefono_u=None,
            password=None,
            municipio_u=None,
            colonia_u=None,
            tipo_u=None,
            imagen=None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            id_usuario=user_data.id_usuario
            nombre_u=user_data.nombre_u
            email_u=user_data.email_u
            telefono_u=user_data.telefono_u
            password=user_data.password
            municipio_u=user_data.municipio_u
            colonia_u=user_data.colonia_u
            tipo_u=user_data.tipo_u
            imagen=user_data.imagen
            # user_hash
            if user_hash == '12345':
                if action is None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(id_usuario)
                elif action == 'put':
                    return self.put(nombre_u,email_u,telefono_u,password,municipio_u,colonia_u,tipo_u,imagen)
                elif action == 'delete':
                    return self.delete(id_usuario)
                elif action == 'update':
                    return self.update(id_usuario, nombre_u,email_u,telefono_u,password,municipio_u,colonia_u,tipo_u,imagen)
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
