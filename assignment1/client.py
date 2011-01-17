#!/usr/bin/python

import socket

host ='block115384-uav.blueboxgrid.com'
port = 54321

size = 1024

number1 = '12345'
number2 = '4321'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host,port))
h = '%016d' % len(number1)
print h
s.send(h)
s.send('12345')

h = '%032d' % len(number2)
s.send(h)
s.send('4321')
s.recv(1024)
s.close()
print 'Received:', data
