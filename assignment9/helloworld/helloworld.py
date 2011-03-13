import sys
import models

print 'Content-Type: text/plain'
print ''
print 'Hello, world! This is amazing!!' + str(sys.path)


games = models.Game.all()

for game in games:
    print game.title
