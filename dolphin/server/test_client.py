#!/usr/bin/env python
from socket import *

HOST = '192.168.59.103'
PORT = 8000

BUF_SIZE = 1024
ADDR = (HOST,PORT)

tcp_client_sock = socket(AF_INET, SOCK_STREAM)
tcp_client_sock.connect(ADDR)

while True:
	data = raw_input('Input Data >')
	if not data:
		break
	tcp_client_sock.send(data)
	data = tcp_client_sock.recv(BUF_SIZE)
	if not data:
		break
	print data

tcp_client_sock.close()

