# coding: utf-8

import socket


socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('', 8080))

while True:
    socket.listen(5)
    client, address = socket.accept()
    print ("{} se connecte".format(address))

    response = client.recv(255)
    if response != "":
        print (response)

print ("Fermeture du serveur")

client.close()
stock.close()
