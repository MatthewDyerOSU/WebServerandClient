import socket
import sys

def checkNumArgs(argv):
    if len(argv) != 1 and len(argv) != 2:
        print("Incorrect number of arguments")
        exit(1)

def main():
    args = sys.argv

    checkNumArgs(args)

    if len(args) > 1:
        port = int(args[1])
    else:
        port = 28333

    # Get a socket
    s = socket.socket()

    # Bind the socket to a port: bind()
    # Error handling for bind is from geeksforgeeks.org
    try:
        s.bind(('', port))
    except socket.error as message:
        print('Bind failed. Error Code:'
              + str(message[0]) + ' Message ' 
              + message[1])
        exit(1)

    # Set the socket up to listen: listen()
    s.listen()

    # Accept new connections (returns a tuple)
    while True:
        new_conn = s.accept()
        print(f'New Socket: {new_conn[0]}, Address: {new_conn[1]}')
        new_socket = new_conn[0]

        # Receive the request from client in loop
        while True:
            data = new_socket.recv(4096)
            decoded = data.decode("ISO-8859-1")
            if decoded == "\r\n\r\n":
                break

        res = ('HTTP/1.1 200 OK\r\n'
                    'Content-Type: text/plain\r\n'
                    'Content-Length: 6\r\n'
                    'Connection: close\r\n'
                    '\r\n'
                    'Hello!\r\n'
                    '\r\n')
        
        # Send the response
        bytes = res.encode("ISO-8859-1")
        s.sendall(bytes)

        # Close the new socket
        new_socket.close()

    # End loop


if __name__ == "__main__":
    main()