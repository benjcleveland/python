#!/usr/bin/python
'''
Module for socket functions that are shared between the client and server
Author - Ben Cleveland
'''

import socket

HEADER_LENGTH = 16

def create_listen_socket(host, port):
    '''
    Creates a listen socket on the given hostname and port
    returns the created socket
    '''

    # create the socket
    sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

    # bind to the port
    sock.bind((host,port))
    sock.listen(5)

    # return the created socket
    return sock

def create_connection(host, port):
    '''
    Creates a client socket connection to the given hostname and port
    Returns the created socket
    '''

    sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host,port))

    return sock

def send_number( conn,  num ):
    ''' 
    sends a given number of the socket connection
    '''
    # figure out the header size
    header_size = '%016d' % len(str(num))
    
    # send the header
    conn.send(header_size)

    # send the number
    conn.send(str(num))

def send_exit( conn ):
    '''
    Client sends this message (header size of -1) to the server telling it the client is done
    '''
    header_size = '%016d' % -1
    conn.send(header_size)


def recv_header( conn ):
    '''
    Recieves the message header from the socket 
    '''
    status = 0
    
    msg_length = read_socket( conn, HEADER_LENGTH) 

    if len(msg_length) != HEADER_LENGTH:
        # error
        print 'Invalid message header length(', len(msg_length), '), closing connection...'
        status = -1
    
    return (status, msg_length )

def recv_number( conn, size ):
    '''
    Recieves the number from the socket 
    '''

    status = 0
    
    # recv the number 
    number = read_socket( conn, size )

    if len(number) != size:
        # error 
        print 'Invalid number length', len(number), ', expected size', size, 'closing connection...'    
        status = -1

    # try to convert the number to a float
    try:
        float(number)
    except:
        print 'Unable to convert number', number, 'closing connection...'
        status = -1

    return (status, number)    

def read_socket( conn, size ):
    '''
    This function reads the given size from the socket and returns the data
    '''
    data = '' 

    while size > 0:
        try:
            data += conn.recv( size )
        except:
            data = ''
            break

        if( len(data) > 0 ):
            size -= len(data) 
        else:   # make sure the thread doesn't hang forever
            break

    return data

if __name__  == '__main__':
    print 'This module cannot be executed directly, exiting'
