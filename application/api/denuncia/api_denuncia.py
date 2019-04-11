import web
import config
import json


class Api_denuncia:
    def get(self, id_denuncia):
        try:
            # http://0.0.0.0:8080/api_denuncia?user_hash=12345&action=get
            if id_denuncia is None:
                result = config.model.get_all_denuncia()
                denuncia_json = []
                for row in result:
                    tmp = dict(row)
                    denuncia_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(denuncia_json)
            else:
                # http://0.0.0.0:8080/api_denuncia?user_hash=12345&action=get&id_denuncia=1
                result = config.model.get_denuncia(int(id_denuncia))
                denuncia_json = []
                denuncia_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(denuncia_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            denuncia_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(denuncia_json)

# http://0.0.0.0:8080/api_denuncia?user_hash=12345&action=put&id_denuncia=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=0
    def put(self, nombre_d,descripcion_d,municipio_d,colonia_d,imagen):
        try:
            config.model.insert_denuncia(nombre_d,descripcion_d,municipio_d,colonia_d,imagen)
            denuncia_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(denuncia_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_denuncia?user_hash=12345&action=delete&id_denuncia=1
    def delete(self, id_denuncia):
        try:
            config.model.delete_denuncia(id_denuncia)
            denuncia_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(denuncia_json)
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_denuncia?user_hash=12345&action=update&id_denuncia=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=default.jpg
    def update(self, id_denuncia, nombre_d,descripcion_d,municipio_d,colonia_d,imagen):
        try:
            config.model.edit_denuncia(id_denuncia,nombre_d,descripcion_d,municipio_d,colonia_d,imagen)
            denuncia_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(denuncia_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            denuncia_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(denuncia_json)

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            id_denuncia=None,
            nombre_d=None,
            descripcion_d=None,
            municipio_d=None,
            colonia_d=None,
            imagen=None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            id_denuncia=user_data.id_denuncia
            nombre_d=user_data.nombre_d
            descripcion_d=user_data.descripcion_d
            municipio_d=user_data.municipio_d
            colonia_d=user_data.colonia_d
            imagen=user_data.imagen
            # user_hash
            if user_hash == '12345':
                if action is None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(id_denuncia)
                elif action == 'put':
                    return self.put(nombre_d,descripcion_d,municipio_d,colonia_d,imagen)
                elif action == 'delete':
                    return self.delete(id_denuncia)
                elif action == 'update':
                    return self.update(id_denuncia, nombre_d,descripcion_d,municipio_d,colonia_d,imagen)
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
