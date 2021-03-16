import socket

DEFAULT_BUF_SIZE = 4
BYTEORDER_LITTLE = 'little'
BYTEORDER_BIG = 'big'
DEFAULT_ENCODING = 'utf-8'

def send_int(some_socket: socket.socket, value: int, length: int = DEFAULT_BUF_SIZE, byteorder: str = BYTEORDER_LITTLE):
    some_socket.send(value.to_bytes(length, byteorder, signed=True))

def send_str(some_socket: socket.socket, message: str):
    encoded_message = message.encode(DEFAULT_ENCODING)
    value = len(encoded_message)
    send_int(some_socket, value)
    some_socket.send(encoded_message)
    pass

def receive_int(some_socket: socket.socket, bufsize: int = DEFAULT_BUF_SIZE, byteorder: str = BYTEORDER_LITTLE):
    return int.from_bytes(some_socket.recv(bufsize), byteorder, signed=True)

def receive_str(some_socket: socket.socket):
    bufsize = receive_int(some_socket)
    return some_socket.recv(bufsize).decode(DEFAULT_ENCODING)