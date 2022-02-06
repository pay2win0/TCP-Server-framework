from concurrent.futures import thread
from http import server
import socket
import threading
from urllib import request

IP = 'X.X.X.X'
PORT = XXXX

def main()
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))
    server.listen(5)
    print(f'[X] lISTENING ON {IP}:{PORT}')

    while True:
        client, address = server.accept()
        print(f'[X] Accepted connection from {address[0]}:{address[1]}')
        client_handler.start = threading.Thread(target=handle_client,args=(client,))
            client_handler.start()

    def handle_client(client_socket):
        with client_socket as sock:
        request = sock.recv(1024)
        print(f'[X]') Received: {request.decode("utf-8)}'
        sock.send(b'ACK')

if_name_== '_main_':
    main()

