#!/usr/bin/python

import socket

host ='block115384-uav.blueboxgrid.com'
port = 54321

size = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host,port))
s.send('Hello, world')
data = s.recv(size)
s.close()
print 'Received:', data
