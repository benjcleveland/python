#!/usr/bin/python


import socket


def create_listen_socket(host, port):
    '''
    Creates a listen socket on the given hostname and port
    returns the created socket
    '''

    sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

    sock.bind((host,port))
    sock.listen(5)

    # return the created socket
    return sock

def main():
    '''
    The main funtion for the server
    '''
    print 'hello world!'

    # create the listen socket
    sock = create_listen_socket( socket.gethostname(), 54321 )

    

if __name__  == '__main__':
    # execute main
    main()
