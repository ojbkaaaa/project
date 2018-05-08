import textwrap
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
define('port',default=8230,help='run on the gaven port', type=int)

class ReverHandler(tornado.web.RequestHandler):
	def get(self,input):
		self.write(input[::-1])

class WrapHandler(tornado.web.RequestHandler):
	def post(self):
		text = self.get_argument('text')
		width = self.get_argument('width',40)
		self.write(textwrap.fill(text,int(width)))

class FrobHandler(tornado.web.RequestHandler):
    def head(self, frob_id):
        frob = retrieve_from_db(frob_id)
        if frob is not None:
            self.set_status(200)
        else:
            self.set_status(404)
    def get(self, frob_id):
        frob = retrieve_from_db(frob_id)
        self.write(frob.serialize())

class WidgetHandler(tornado.web.RequestHandler):
    def get(self, widget_id):
        widget = retrieve_from_db(widget_id)
        self.write(widget.serialize())

    def post(self, widget_id):
        widget = retrieve_from_db(widget_id)
        widget['foo'] = self.get_argument('foo')
        save_to_db(widget)

if __name__ == '__main__':
	tornado.options.parse_command_line()
	app = tornado.web.Application(
		handlers=[
			(r"/widget/(\d+)", WidgetHandler),
			(r'/reverse/(\w+)',ReverHandler),
			(r'/wrap', WrapHandler),
			(r"/frob/(\d+)", FrobHandler)
		]
	)
	http_server = tornado.httpserver.HTTPServer(app)
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()

