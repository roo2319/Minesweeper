import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print(f"connecting to {server_address[0]} port {server_address[1]}")
sock.connect(server_address)

while True:
    # Send data
    move = str.encode(input("Please enter the coordinates you want to reveal in the form (row,col): "))
    # move = b"2,2"
    print(f"sending '{move.decode()}'")
    sock.sendall(bytes(move))

    data = sock.recv(32).decode()
    print(f"received '{data}'")
