import generation
import socket
import sys
import re

state = generation.State(10,10,10)
print (state)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)

print(f"starting up on {server_address[0]} port {server_address[1]}") 
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)
while True:
    # Wait for a connection
    print(f"waiting for a connection")
    connection, client_address = sock.accept()
    print(f"connection from {client_address}")
    while True:
        data = connection.recv(32).decode()
        print(f"received '{data}'")
        if data:
            # MINESWEEP
            try:
                coords = list(map(int,data.lstrip('(').rstrip(')').split(',')))
                print(coords)
                row, col = coords[0], coords[1]
                res = state.check(row,col)
                if res == '*':
                    print("uh oh, mine")
                    connection.sendall(b"* - Mine! Resetting...")
                    state = generation.State(10,10,10)
                    print (state)
                else:
                    connection.sendall(str.encode(res))
            except:
                connection.sendall(b"INVALID MOVE")
