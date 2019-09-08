#!/usr/local/bin/python3


class Router:
    ALLOWED_METHODS = ('GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'OPTIONS')
    allowed_path_method = {}

    def add_path(self,path,method,func):
        if method in self.ALLOWED_METHODS:
            if path in self.allowed_path_method.keys():
                self.allowed_path_method[path][method] = func
            else:
                self.allowed_path_method = {path: {method: func}}
            print(self.allowed_path_method)
        else:
            return 405, 'Error 405: Method Not Allowed'

    def request(self,path,method):
        if path in self.allowed_path_method.keys():
            if method in self.allowed_path_method[path].keys():
                func_to_call = self.allowed_path_method[path][method]
                return func_to_call(path,method)
            else:
                return 405, 'Error 405: Method Not Allowed'
        else:
            return 404, 'Error 404: Not Found'

        return result

    def get(self, path):
        return self.request(path,'GET')

    def post(self, path):
        return self.request(path,'POST')

    def put(self, path):
        return self.request(path,'PUT')

    def patch(self, path):
        return self.request(path,'PATCH')

    def delete(self, path):
        return self.request(path,'DELETE')


if __name__ == '__main__':


    def my_info(path, method):
        return 200, {"me": "Joanne"}


    def update_me(path, method):
        return 200, "OK"

    router = Router()
    router.add_path('/me', 'GET', my_info)
    router.add_path('/me', 'UPDATE', update_me)
    router.add_path('/me', 'FIRE', update_me)
    print(router.request('/me', 'GET'))
    print(router.request('/me', 'UPDATE'))
    print(router.request('/you', 'POST'))
    print(router.get('/me'))

