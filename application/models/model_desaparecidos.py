import web
import config

db = config.db


def get_all_desaparecidos():
    try:
        return db.select('desaparecidos')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_desaparecidos(id_desaparecidos):
    try:
        return db.select('desaparecidos', where='id_desaparecidos=$id_desaparecidos', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_desaparecidos(id_desaparecidos):
    try:
        return db.delete('desaparecidos', where='id_desaparecidos=$id_desaparecidos', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_desaparecidos(nombre_p,email_p,telefono_p,municipio_p,colonia_p,fecha_p,nombre_m,edad_m,sexo_m,tipo_m,descripcion_m,id_usuario,imagen):
    try:
        return db.insert('desaparecidos',nombre_p=nombre_p,
email_p=email_p,
telefono_p=telefono_p,
municipio_p=municipio_p,
colonia_p=colonia_p,
fecha_p=fecha_p,
nombre_m=nombre_m,
edad_m=edad_m,
sexo_m=sexo_m,
tipo_m=tipo_m,
descripcion_m=descripcion_m,
id_usuario=id_usuario,
imagen=imagen)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_desaparecidos(id_desaparecidos,nombre_p,email_p,telefono_p,municipio_p,colonia_p,fecha_p,nombre_m,edad_m,sexo_m,tipo_m,descripcion_m,id_usuario):
    try:
        return db.update('desaparecidos',id_desaparecidos=id_desaparecidos,
nombre_p=nombre_p,
email_p=email_p,
telefono_p=telefono_p,
municipio_p=municipio_p,
colonia_p=colonia_p,
fecha_p=fecha_p,
nombre_m=nombre_m,
edad_m=edad_m,
sexo_m=sexo_m,
tipo_m=tipo_m,
descripcion_m=descripcion_m,
id_usuario=id_usuario,
                  where='id_desaparecidos=$id_desaparecidos',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
