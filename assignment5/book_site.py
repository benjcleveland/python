#!/usr/bin/python

'''
    Basic webite using cherrypy.
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

    def index(self):
        '''
        handle the index page
        Displays a list books in the database that link to additional information
        '''

        tmpl = self.loader.load('index.html')
    
        return tmpl.generate(title='Library', links=self.bdb.titles()).render('html', doctype='html') 

    def book(self, id):
        '''
        handle the book page.
        Will render the book information based on the id that is passed
        '''

        title_info = bookdb.BookDB().title_info(id)

        tmpl = self.loader.load('book.html')
   
        return tmpl.generate(title='Book Info', book=title_info).render('html', doctype='html') 

    book.exposed = True
    index.exposed = True

# cherrypy site configuration
booksite_config  = os.path.join(os.path.dirname(__file__), 'book_site.conf')

if __name__ == '__main__':
    # start the cherry py web framework
    cherrypy.quickstart(booksite(), config=booksite_config)
