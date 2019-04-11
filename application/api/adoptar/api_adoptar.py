import web
import config
import json


class Api_adoptar:
    def get(self, id_publicar):
        try:
            # http://0.0.0.0:8080/api_adoptar?user_hash=12345&action=get
            if id_publicar is None:
                result = config.model.get_all_adoptar()
                adoptar_json = []
                for row in result:
                    tmp = dict(row)
                    adoptar_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(adoptar_json)
            else:
                # http://0.0.0.0:8080/api_adoptar?user_hash=12345&action=get&id_publicar=1
                result = config.model.get_adoptar(int(id_publicar))
                adoptar_json = []
                adoptar_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(adoptar_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            adoptar_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(adoptar_json)

# http://0.0.0.0:8080/api_adoptar?user_hash=12345&action=put&id_publicar=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=0
    def put(self, nom_persona,email,telefono,municipio,colonia,fecha,nom_mascota,edad_mascota,sexo_mascota,tipo_mascota,descripcion_mascota,id_usuario,imagen):
        try:
            config.model.insert_adoptar(nom_persona,email,telefono,municipio,colonia,fecha,nom_mascota,edad_mascota,sexo_mascota,tipo_mascota,descripcion_mascota,id_usuario,imagen)
            adoptar_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(adoptar_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_adoptar?user_hash=12345&action=delete&id_publicar=1
    def delete(self, id_publicar):
        try:
            config.model.delete_adoptar(id_publicar)
            adoptar_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(adoptar_json)
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_adoptar?user_hash=12345&action=update&id_publicar=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=default.jpg
    def update(self, id_publicar, nom_persona,email,telefono,municipio,colonia,fecha,nom_mascota,edad_mascota,sexo_mascota,tipo_mascota,descripcion_mascota,id_usuario,imagen):
        try:
            config.model.edit_adoptar(id_publicar,nom_persona,email,telefono,municipio,colonia,fecha,nom_mascota,edad_mascota,sexo_mascota,tipo_mascota,descripcion_mascota,id_usuario,imagen)
            adoptar_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(adoptar_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            adoptar_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(adoptar_json)

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            id_publicar=None,
            nom_persona=None,
            email=None,
            telefono=None,
            municipio=None,
            colonia=None,
            fecha=None,
            nom_mascota=None,
            edad_mascota=None,
            sexo_mascota=None,
            tipo_mascota=None,
            descripcion_mascota=None,
            id_usuario=None,
            imagen=None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            id_publicar=user_data.id_publicar
            nom_persona=user_data.nom_persona
            email=user_data.email
            telefono=user_data.telefono
            municipio=user_data.municipio
            colonia=user_data.colonia
            fecha=user_data.fecha
            nom_mascota=user_data.nom_mascota
            edad_mascota=user_data.edad_mascota
            sexo_mascota=user_data.sexo_mascota
            tipo_mascota=user_data.tipo_mascota
            descripcion_mascota=user_data.descripcion_mascota
            id_usuario=user_data.id_usuario
            imagen=user_data.imagen
            # user_hash
            if user_hash == '12345':
                if action is None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(id_publicar)
                elif action == 'put':
                    return self.put(nom_persona,email,telefono,municipio,colonia,fecha,nom_mascota,edad_mascota,sexo_mascota,tipo_mascota,descripcion_mascota,id_usuario,imagen)
                elif action == 'delete':
                    return self.delete(id_publicar)
                elif action == 'update':
                    return self.update(id_publicar, nom_persona,email,telefono,municipio,colonia,fecha,nom_mascota,edad_mascota,sexo_mascota,tipo_mascota,descripcion_mascota,id_usuario,imagen)
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
