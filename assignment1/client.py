#!/usr/bin/python

import libsocket


def add_numbers( sock ):
    '''
    gets two numbers from the user to be added by the server
    '''
    status = -1 
    number1 = number2 = '' 
    # get two numbers from the user
    while status == -1:
        (status, number1) = get_user_number('Enter number one -> ')

    # reset the status 
    status = -1
    while status == -1:
        (status, number2) = get_user_number('Enter number two -> ')

    # send the numbers to the server
    libsocket.send_number( sock, number1)
    libsocket.send_number( sock, number2)

    # recv the result
    (status, msg_length) = libsocket.recv_header( sock )       
    if status == 0:
        (status, result) = libsocket.recv_number( sock, long(msg_length))
        if status == 0:
            print '\nResult:', number1, '+', number2, '=', result

    if status != 0:
        # we ran into an error, close the connection and exit
        sock.close()
        exit()

def get_user_number( disp_str ):
    ''' 
    Getsa number from the user
    '''
    status = 0 
    number = raw_input(disp_str)

    try:
        float(number)
    except:
        print 'Invalid number entered,', number
        status = -1
    
    return (status, number)
def menu():
    '''
    Display the user input menu
    '''
    
    print '\nWecome to the adding machine'
    print '1. Add two numbers'
    print '2. Exit'

    return raw_input('Enter Selection-> ')

def main():
    '''
    Main entry point for the client program
    '''

    host ='block115384-uav.blueboxgrid.com'
    port = 62000 
    user_input = ''

    # connect to the server
    try:
        sock = libsocket.create_connection(host, port)
    except:
        print 'Could not connect to the server, exiting...'
        exit()

    print 'Successfully connected to the server'
    
    while user_input != '2':
        # display the menu
        user_input = menu()
        
        if user_input == '1':
            add_numbers( sock )
        elif user_input != '2':
            print '\nInvalid Selection...\n'

    # tell the server we are exiting
    libsocket.send_exit(sock)

    # close the connection
    sock.close()

if __name__ == '__main__':
    # Execute main
    main()
