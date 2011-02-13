#!/usr/bin/python

import cherrypy

class bookOne(object):
    def index(self):
        return 'book one!'
    index.exposed = True

class booksite(object):
    bookone = bookOne()
    def index(self):
        return 'Hello world!'
    index.exposed = True

import os.path
booksite_config  = os.path.join(os.path.dirname(__file__), 'book_site.conf')

if __name__ == '__main__':
    # start the cherry py web framework
    cherrypy.quickstart(booksite(), config=booksite_config)
