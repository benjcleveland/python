#!/usr/bin/python

import socket

host ='block115384-uav.blueboxgrid.com'
port = 62000 

size = 1024

number1 = '12345'
number2 = '4321'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host,port))
h = '%016d' % len(number1)
print h
s.send(h)
s.send('12345')

h = '%016d' % len(number2)
s.send(h)
s.send('4321')
data =  s.recv(1024)
print 'Received:', data
data =  s.recv(1024)
print 'Received:', data
s.close()
