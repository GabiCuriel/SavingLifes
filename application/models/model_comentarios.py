import web
import config

db = config.db


def get_all_comentarios():
    try:
        return db.select('comentarios')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_comentarios(id_comentario):
    try:
        return db.select('comentarios', where='id_comentario=$id_comentario', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_comentarios(id_comentario):
    try:
        return db.delete('comentarios', where='id_comentario=$id_comentario', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_comentarios(nombre,email,comentario):
    try:
        return db.insert('comentarios',nombre=nombre,
email=email,
comentario=comentario)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_comentarios(id_comentario,nombre,email,comentario):
    try:
        return db.update('comentarios',id_comentario=id_comentario,
nombre=nombre,
email=email,
comentario=comentario,
                  where='id_comentario=$id_comentario',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
