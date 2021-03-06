from google.appengine.ext import db

class gameviewer_game(db.Model):
    title = db.StringProperty()
    publisher = db.StringProperty()
    year_published = db.StringProperty()
    description = db.StringProperty()
    last_played = db.DateTimeProperty()
    image_name = db.StringProperty()
    genre = db.StringProperty()
    maxplayers = db.IntegerProperty()
    minplayers = db.IntegerProperty()
    

class gameviewer_rating(db.Model):
    game = db.ReferenceProperty(gameviewer_game)
    rating = db.FloatProperty()
    name = db.StringProperty()
    comment = db.StringProperty(multiline=True)



