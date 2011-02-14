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
        self.loader = genshi.template.TemplateLoader( os.path.join( os.path.dirname(__file__), 'templates'),
                auto_reload=True)

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
            raise cherrypy.HTTPError(404,'404 Not Found')
        
        # get the title info from the database
        title_info = bookdb.BookDB().title_info(id)

        # load the book page template
        tmpl = self.loader.load('book.html')
   
        return tmpl.generate(title='Book Info', book=title_info).render('html', doctype='html') 

# cherrypy site configuration
booksite_config  = os.path.join(os.path.dirname(__file__), 'book_site.conf')

if __name__ == '__main__':
    # start the cherry py web framework
    cherrypy.quickstart(booksite(), config=booksite_config)
