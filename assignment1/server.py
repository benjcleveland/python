#!/usr/bin/python

'''
Adding server - Adds two number from the client then sends back the result

Author - Ben Cleveland
'''

from libsocket import *
from threading import Thread

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
            m_length = long(msg_length)
            if status == 0 and m_length > 0:
                # read the number
                (status, numbers[i]) = recv_number( conn, m_length )
                if status != 0:
                    break
            else:
                break

        # check status
        if status == 0 and m_length > 0:
            # add both number together and send back to the client
            result = float(numbers[0]) + float(numbers[1])
            print 'adding', numbers[0], '+', numbers[1], '=', result

            # send the result to the client
            send_number( conn, result )

        else:
            break

    # close the connection when finished
    print 'Thread for', addr, 'exiting...'

    conn.close()

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
