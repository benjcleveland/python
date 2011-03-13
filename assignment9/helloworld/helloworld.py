import models
import datetime
from google.appengine.ext import webapp
from google.appengine.ext.bulkload import transform
from google.appengine.ext.webapp.util import run_wsgi_app

class MainPage(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('Hello, webapp World!')

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

