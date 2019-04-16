import web
import config

db = config.db


def get_all_denuncia():
    try:
        return db.select('denuncia')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_denuncia(id_denuncia):
    try:
        return db.select('denuncia', where='id_denuncia=$id_denuncia', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_denuncia(id_denuncia):
    try:
        return db.delete('denuncia', where='id_denuncia=$id_denuncia', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_denuncia(descripcion_d,calle_d,municipio_d,colonia_d,longitud,latitud):
    try:
        return db.insert('denuncia',descripcion_d=descripcion_d,
calle_d=calle_d,
municipio_d=municipio_d,
colonia_d=colonia_d,
longitud=longitud,
latitud=latitud)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_denuncia(id_denuncia,descripcion_d,calle_d,municipio_d,colonia_d,longitud,latitud):
    try:
        return db.update('denuncia',id_denuncia=id_denuncia,
descripcion_d=descripcion_d,
calle_d=calle_d,
municipio_d=municipio_d,
colonia_d=colonia_d,
longitud=longitud,
latitud=latitud,
                  where='id_denuncia=$id_denuncia',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
