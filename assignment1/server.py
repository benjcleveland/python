#!/usr/bin/python

import socket
from threading import Thread

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
    print 'in thread',conn, addr

    # do nothing for now
    while True:
        pass

    # close the connection when finished
    conn.close()

def main():
    '''
    The main funtion for the server
    '''
    print 'adding server'

    # create the listen socket
    sock = create_listen_socket( socket.gethostname(), 54321 )

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
