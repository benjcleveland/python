#!/usr/bin/python
from google.appengine.ext import db
from google.appengine.tools import bulkloader


class Game(db.Model):
    title = db.StringProperty()
    publisher = db.StringProperty()

class GameLoader(bulkloader.Loader):
    def __init__(self):
        bulkloader.Loader.__init__(self, 'Game',
                                [('title', str),
                                ('publisher', str),
                                ])


loaders = [GameLoader]




