import web
import config
import json


class Api_desaparecidos:
    def get(self, id_desaparecidos):
        try:
            # http://0.0.0.0:8080/api_desaparecidos?user_hash=12345&action=get
            if id_desaparecidos is None:
                result = config.model.get_all_desaparecidos()
                desaparecidos_json = []
                for row in result:
                    tmp = dict(row)
                    desaparecidos_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(desaparecidos_json)
            else:
                # http://0.0.0.0:8080/api_desaparecidos?user_hash=12345&action=get&id_desaparecidos=1
                result = config.model.get_desaparecidos(int(id_desaparecidos))
                desaparecidos_json = []
                desaparecidos_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(desaparecidos_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            desaparecidos_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(desaparecidos_json)

# http://0.0.0.0:8080/api_desaparecidos?user_hash=12345&action=put&id_desaparecidos=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=0
    def put(self, nombre_p,email_p,telefono_p,municipio_p,colonia_p,fecha_p,nombre_m,edad_m,sexo_m,tipo_m,descripcion_m,id_usuario,imagen):
        try:
            config.model.insert_desaparecidos(nombre_p,email_p,telefono_p,municipio_p,colonia_p,fecha_p,nombre_m,edad_m,sexo_m,tipo_m,descripcion_m,id_usuario,imagen)
            desaparecidos_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(desaparecidos_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_desaparecidos?user_hash=12345&action=delete&id_desaparecidos=1
    def delete(self, id_desaparecidos):
        try:
            config.model.delete_desaparecidos(id_desaparecidos)
            desaparecidos_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(desaparecidos_json)
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_desaparecidos?user_hash=12345&action=update&id_desaparecidos=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=default.jpg
    def update(self, id_desaparecidos, nombre_p,email_p,telefono_p,municipio_p,colonia_p,fecha_p,nombre_m,edad_m,sexo_m,tipo_m,descripcion_m,id_usuario,imagen):
        try:
            config.model.edit_desaparecidos(id_desaparecidos,nombre_p,email_p,telefono_p,municipio_p,colonia_p,fecha_p,nombre_m,edad_m,sexo_m,tipo_m,descripcion_m,id_usuario,imagen)
            desaparecidos_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(desaparecidos_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            desaparecidos_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(desaparecidos_json)

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            id_desaparecidos=None,
            nombre_p=None,
            email_p=None,
            telefono_p=None,
            municipio_p=None,
            colonia_p=None,
            fecha_p=None,
            nombre_m=None,
            edad_m=None,
            sexo_m=None,
            tipo_m=None,
            descripcion_m=None,
            id_usuario=None,
            imagen=None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            id_desaparecidos=user_data.id_desaparecidos
            nombre_p=user_data.nombre_p
            email_p=user_data.email_p
            telefono_p=user_data.telefono_p
            municipio_p=user_data.municipio_p
            colonia_p=user_data.colonia_p
            fecha_p=user_data.fecha_p
            nombre_m=user_data.nombre_m
            edad_m=user_data.edad_m
            sexo_m=user_data.sexo_m
            tipo_m=user_data.tipo_m
            descripcion_m=user_data.descripcion_m
            id_usuario=user_data.id_usuario
            imagen=user_data.imagen
            # user_hash
            if user_hash == '12345':
                if action is None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(id_desaparecidos)
                elif action == 'put':
                    return self.put(nombre_p,email_p,telefono_p,municipio_p,colonia_p,fecha_p,nombre_m,edad_m,sexo_m,tipo_m,descripcion_m,id_usuario,imagen)
                elif action == 'delete':
                    return self.delete(id_desaparecidos)
                elif action == 'update':
                    return self.update(id_desaparecidos, nombre_p,email_p,telefono_p,municipio_p,colonia_p,fecha_p,nombre_m,edad_m,sexo_m,tipo_m,descripcion_m,id_usuario,imagen)
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
