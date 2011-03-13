from google.appengine.ext import db

class Game(db.Model):
    title = db.StringProperty()
    publisher = db.StringProperty()

