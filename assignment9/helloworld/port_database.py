#!/usr/bin/python

import sys
from dev_appserver import fix_sys_path
fix_sys_path()

import psycopg2

from google.appengine.ext import db
from google.appengine.tools import bulkloader

sys.path.append('/home/cleveb/git/python/assignment9/helloworld/psycopg2')
class Game(db.Model):
    title = db.StringProperty()

class GameLoader(buildloader.Loader):
    def __init__(self):
        bulkloader.Loader.__init__(self, 'Game',
                                [('title', str),
                                ])

# connetc to the boardgame database

conn = psycopg2.connect('dbname=boardgames user=cleveb')
cur = conn.cursor()

cur.execute( 'select title from gameviewer_game;')

#print cur.fetchall()

loaders = [GameLoader]
'''
for game in cur:
   g = Games() 
   print game[0]
   g.title = game[0]
   print g.title
   g.put()


# get all the games out
games = Games.all() 
for g in games:
    if g.title:
        print g.title
        '''




