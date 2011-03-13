#!/usr/bin/python
from google.appengine.ext import db
from google.appengine.tools import bulkloader

class Game(db.Model):
    title = db.StringProperty()
    publisher = db.StringProperty()

