import tornado.web
import tornado.ioloop


class HandlerPost(tornado.web.RequestHandler):

    def post(self):
        a = self.get_argument('username')
        self.write(a)


class HandlerGet_body(tornado.web.RequestHandler):

    def get(self):
        a = self.get_argument('username')
        self.write(a)


class HandlerDel(tornado.web.RequestHandler):

    def delete(self):
        a = self.get_argument('username')
        self.write(a)


class HandlerPut(tornado.web.RequestHandler):

    def put(self):
        a = self.get_argument('username')
        self.write(a)


class HandlerDuplicate(tornado.web.RequestHandler):

    def get(self):
        a = self.get_argument('username')
        self.write(a)


if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/get_key", HandlerPost),
        (r"/get_body", HandlerGet_body),
        (r"/delete_body", HandlerDel),
        (r"/update_body", HandlerPut),
        (r"/duplicate", HandlerDuplicate)
    ])
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
