import socket
import threading
import tkinter as tk

def recv_msg(udp_socket):
    while True:
        recv_data = udp_socket.recvfrom(1024)
        msg = recv_data[0].decode('utf-8')
        send_addr = recv_data[1][0]
        print(send_addr)

def send_msg(udp_socket,dest_ip,dest_port):
    while True:
        send_data = input('输入要发送的信息:')
        udp_socket.sendto(send_data.encode('utf-8'),(dest_ip,dest_port))

if __name__ == '__main__':
    #创建套接字
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #绑定本地信息
    udp_socket.bind(('',7788))
    #对方ip
    dest_ip = '192.168.108.29'
    dest_port = '8080'

    # recv_msg(udp_socket)
    # send_msg(udp_socket,dest_ip,dest_port)
    t_recv = threading.Thread(target=recv_msg,args=(udp_socket,))
    t_send = threading.Thread(target=send_msg,args=(udp_socket,dest_ip,dest_port))

    t_recv.start()
    t_send.start()
    udp_socket.close()#关闭套接字