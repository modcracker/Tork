#!/usr/bin/python

import os
import sys
sys.dont_write_bytecode = True
import tornado.auth
import tornado.escape
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

from config.settings import get_routes, get_settings

class Application(tornado.web.Application):
  def __init__(self):
    handlers, settings = get_routes(), get_settings()
    tornado.web.Application.__init__(self, handlers, **settings)
    
def main():
  tornado.options.parse_command_line()
  http_server = tornado.httpserver.HTTPServer(Application())
  http_server.listen(options.port)
  tornado.ioloop.IOLoop.instance().start()
  
if __name__ == '__main__':
  main()