#!/usr/bin/python

import socket
import sys
from threading import Thread

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

def handle_connection( conn, addr ):
    '''
    handles reading and writing to and from the socket
    '''
    
    status = 0
    numbers = [0,0]
    print 'Spawned thread for ', addr

    # do nothing for now
    while True:
        # recv both numbers
        for i in range(2):
            # read the header
            (status, msg_length) = recv_header( conn )
            if status == 0:
                # read the number
                (status, numbers[i]) = recv_number( conn, long(msg_length ))
                if status != 0:
                    break
            else:
                break

        # check status
        if status == 0:
            # add both number together and send back to the client
            result = long(numbers[0]) + long(numbers[1])
            print 'adding', numbers[0], '+', numbers[1], '=', result

            # send the result to the client
            send_number( conn, result )

        else:
            break

    # close the connection when finished
    conn.close()

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

def recv_header( conn ):
    '''
    Recieves the message header from the socket 
    '''
    status = 0
    
    msg_length = read_socket( conn, HEADER_LENGTH) 

    if len(msg_length) > 0:
        print 'Next message length:', msg_length
    else:
        print 'Invalid message header length(', msg_length, '), closing connection...'

        status = -1
    
    return (status, msg_length )

def recv_number( conn, size ):
    '''
    Recieves the number from the socket 
    '''

    status = 0
    print size

    # recv the number 
    number = read_socket( conn, size )

    if len(number) == size:
        print 'Read number:', number
    else:
        # error 
        print 'Invalid number length', len(number), ', expected size', size, 'closing connection'    
        status = -1

    return (status, number)    

def read_socket( conn, size ):
    '''
    This function reads the given size from the socket and returns the data
    '''
    data = '' 

    while size > 0:
        data += conn.recv( size )
        size -= len(data) 

    return data

def main():
    '''
    The main funtion for the server
    '''
    print 'adding server'

    # create the listen socket
    sock = create_listen_socket( socket.gethostname(), 62000 )

    # await for a connection
    while True:
        conn, addr = sock.accept()
        print 'Received connection from ', addr

        # create a thread to handle the connection
        t = Thread(target = handle_connection, args=(conn,addr)) 

        # start the thread
        t.start()

if __name__  == '__main__':
    # execute main
    main()
