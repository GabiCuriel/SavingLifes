import web
import config
import json


class Api_users:
    def get(self, username):
        try:
            # http://0.0.0.0:8080/api_users?user_hash=12345&action=get
            if username is None:
                result = config.model.get_all_users()
                users_json = []
                for row in result:
                    tmp = dict(row)
                    users_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(users_json)
            else:
                # http://0.0.0.0:8080/api_users?user_hash=12345&action=get&username=1
                result = config.model.get_users(int(username))
                users_json = []
                users_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(users_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            users_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(users_json)

# http://0.0.0.0:8080/api_users?user_hash=12345&action=put&username=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=0
    def put(self, password,privilege,status,name,email,other_data,user_hash,change_pwd,created):
        try:
            config.model.insert_users(password,privilege,status,name,email,other_data,user_hash,change_pwd,created)
            users_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(users_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_users?user_hash=12345&action=delete&username=1
    def delete(self, username):
        try:
            config.model.delete_users(username)
            users_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(users_json)
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_users?user_hash=12345&action=update&username=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=default.jpg
    def update(self, username, password,privilege,status,name,email,other_data,user_hash,change_pwd,created):
        try:
            config.model.edit_users(username,password,privilege,status,name,email,other_data,user_hash,change_pwd,created)
            users_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(users_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            users_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(users_json)

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            username=None,
            password=None,
            privilege=None,
            status=None,
            name=None,
            email=None,
            other_data=None,
            user_hash=None,
            change_pwd=None,
            created=None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            username=user_data.username
            password=user_data.password
            privilege=user_data.privilege
            status=user_data.status
            name=user_data.name
            email=user_data.email
            other_data=user_data.other_data
            user_hash=user_data.user_hash
            change_pwd=user_data.change_pwd
            created=user_data.created
            # user_hash
            if user_hash == '12345':
                if action is None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(username)
                elif action == 'put':
                    return self.put(password,privilege,status,name,email,other_data,user_hash,change_pwd,created)
                elif action == 'delete':
                    return self.delete(username)
                elif action == 'update':
                    return self.update(username, password,privilege,status,name,email,other_data,user_hash,change_pwd,created)
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
