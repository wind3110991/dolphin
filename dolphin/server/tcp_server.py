#!/usr/bin/python
#-*- coding:utf-8 -*-

#import select                                                                                                                          
from socket import *
import Queue
from time import ctime
import os

HOST = '172.17.0.116'
PORT = 8000
BUF_SIZE = 1024
TIMEOUT = 20 
ADDR = (HOST,PORT)

tcp_svr_sock = socket(AF_INET, SOCK_STREAM)
tcp_svr_sock.bind(ADDR)
tcp_svr_sock.listen(5)


if __name__ == "__main__":
	while True:
		print 'wating for connection...'
		tcp_client_sock, addr = tcp_svr_sock.accept()
		print "Connecting from %s, fd number: %s" % (addr[0], addr[1])
		while True:
			data = tcp_client_sock.recv(BUF_SIZE)
			print "Receive data from %s" % addr[0]
			print "Data Context: %s" % data
			if not data:
				break
			tcp_client_sock.send('Data from server: time[%s] \n Data: %s'%(ctime(), data))
		tcp_client_sock.close()

	tcp_svr_sock.close()

main()
#创建socket 套接字

# BUF_MAX = 1024
# HOST = '127.0.0.1'
# PORT = 8888
# TIMEOUT = 20


# server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# server.setblocking(False)
# #配置参数
# server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR  , 1)
# server_address= (HOST, PORT)
# server.bind(server_address)
# server.listen(BUF_MAX)
# inputs = [server]
# outputs = []
# message_queues = {}

# while inputs:
#     print "waiting for next event"
# #    readable , writable , exceptional = select.select(inputs, outputs, inputs, timeout)  最后一个是超时，当前连接要是超过这个时间的话，就会kill
#     readable , writable , exceptional = select.select(inputs, outputs, inputs)
                                                                                                                                                        
#     # When timeout reached , select return three empty lists
#     if not (readable or writable or exceptional):
#         print "Time out ! "
#         break;
#     for s in readable:
#         if s is server:
#             #通过inputs查看是否有客户端来
#             connection, client_address = s.accept()
#             print "connection from ", client_address
#             connection.setblocking(0)
#             inputs.append(connection)
#             message_queues[connection] = Queue.Queue()
#         else:
#             data = s.recv(1024)
#             if data :
#                 print " received " , data , "from ",s.getpeername()
#                 message_queues[s].put(data)
#                 # Add output channel for response
#                 if s not in outputs:
#                     outputs.append(s)
#             else:
#                 #Interpret empty result as closed connection
#                 print "closing", client_address
#                 if s in outputs:
#                     outputs.remove(s)
#                 inputs.remove(s)
#                 s.close()
#                 #清除队列信息
#                 del message_queues[s]
#     for s in writable:
#         try:
#             next_msg = message_queues[s].get_nowait()
#         except Queue.Empty:
#             print " ", s.getpeername(), 'queue empty'
#             outputs.remove(s)
#         else:
#             print " sending ", next_msg, " to ", s.getpeername()
#             os.popen('sleep 5').read()
#             s.send(next_msg)
                                                                                                                                                            
#     for s in exceptional:
#         print " exception condition on ", s.getpeername()
#         #stop listening for input on the connection
#         inputs.remove(s)
#         if s in outputs:
#             outputs.remove(s)
#         s.close()
#         #清除队列信息
#         del message_queues[s]
