import web
import config

db = config.db


def get_all_adoptar():
    try:
        return db.select('adoptar')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_adoptar(id_publicar):
    try:
        return db.select('adoptar', where='id_publicar=$id_publicar', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_adoptar(id_publicar):
    try:
        return db.delete('adoptar', where='id_publicar=$id_publicar', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_adoptar(nom_persona,email,telefono,municipio,colonia,fecha,nom_mascota,edad_mascota,sexo_mascota,tipo_mascota,descripcion_mascota,id_usuario,imagen):
    try:
        return db.insert('adoptar',nom_persona=nom_persona,
email=email,
telefono=telefono,
municipio=municipio,
colonia=colonia,
fecha=fecha,
nom_mascota=nom_mascota,
edad_mascota=edad_mascota,
sexo_mascota=sexo_mascota,
tipo_mascota=tipo_mascota,
descripcion_mascota=descripcion_mascota,
id_usuario=id_usuario,
imagen=imagen)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_adoptar(id_publicar,nom_persona,email,telefono,municipio,colonia,fecha,nom_mascota,edad_mascota,sexo_mascota,tipo_mascota,descripcion_mascota,id_usuario):
    try:
        return db.update('adoptar',id_publicar=id_publicar,
nom_persona=nom_persona,
email=email,
telefono=telefono,
municipio=municipio,
colonia=colonia,
fecha=fecha,
nom_mascota=nom_mascota,
edad_mascota=edad_mascota,
sexo_mascota=sexo_mascota,
tipo_mascota=tipo_mascota,
descripcion_mascota=descripcion_mascota,
id_usuario=id_usuario,
                  where='id_publicar=$id_publicar',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None

