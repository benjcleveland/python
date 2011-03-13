import models
import datetime
from google.appengine.ext import webapp
from google.appengine.ext.bulkload import transform
from google.appengine.ext.webapp.util import run_wsgi_app

class MainPage(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('Hello, webapp World!')

        g = models.Game()
        g.title = 'title'
        g.publisher = 'publisher'
        g.year_published = '2001'
        g.description = 'description'
        g.last_played = datetime.datetime.now()
        g.image_name = 'image_name'
        g.genre = 'genretest'
        g.maxplayers = 10
        g.minplayers = 1

        g.put()

        r = models.Rating()
        r.game = g
        r.rating = 7.2
        r.name = 'name'
        r.comment = 'comment'

        r.put()

        self.response.out.write(dir(transform))
        games = models.Game.all()
        for game in games:
#            self.response.out.write(' '.join([game.title, game.publisher,'\n']))
            self.response.out.write(game.title + game.genre + game.publisher +'\n')


        rating = models.Rating.all()
        for r in rating:
            self.response.out.write(r.game.title + ' ' + str(r.rating) + ' ' + r.name + ' ' + r.comment + '\n' )

application = webapp.WSGIApplication(
                        [('/', MainPage)],
                        debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()

