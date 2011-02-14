#!/usr/bin/python

'''
    Basic webite using cherrypy.  Uses genshi for html templates.
    Uses the bookdb module for a psuedo backend database
'''

import bookdb
import cherrypy
import genshi.template
import os.path

class booksite(object):

    def __init__(self):
        '''
        initialize the class
        '''
        # hard code the path to the templates to make running in daemon mode easier
        self.loader = genshi.template.TemplateLoader( '/home/cleveb/git/python/assignment5/templates', auto_reload=True)

        # get a copy of the database
        self.bdb = bookdb.BookDB()

    @cherrypy.expose
    def index(self):
        '''
        handle the index page
        Displays a list books in the database that link to additional information
        '''

        tmpl = self.loader.load('index.html')
    
        return tmpl.generate(title='Library', links=self.bdb.titles()).render('html', doctype='html') 

    @cherrypy.expose # equivalent of book.exposed = True
    def book(self, id=None):
        '''
        handle the book page.
        Will render the book information based on the id that is passed
        '''

        if not bookdb.database.has_key(id):
            # make sure this key is in the database
            raise cherrypy.HTTPError(400,'400 Bad Request - Invalid syntax')
        
        # get the title info from the database
        title_info = bookdb.BookDB().title_info(id)

        # load the book page template
        tmpl = self.loader.load('book.html')
   
        return tmpl.generate(title='Book Info', book=title_info).render('html', doctype='html') 

# cherrypy site configuration
booksite_config  = os.path.join(os.path.dirname(__file__), 'book_site.conf')

if __name__ == '__main__':

    # start the process as a daemon
    d = cherrypy.process.plugins.Daemonizer(cherrypy.engine)
    d.subscribe()

    # start the cherry py web framework
    cherrypy.quickstart(booksite(), config=booksite_config)
