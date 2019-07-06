import sys
import socket
import threading

connections = []
addresses = []
def create_socket():
    global host
    global port
    global s
    host = ""
    port = 5568
    s=socket.socket()
def bind_socket():
    global host
    global port
    global s
    s.bind((host,port))
    s.listen(5)
def socket_accept():
    for i in connections:
        i.close()
    del connections[:]
    del addresses[:]
    while True:
        conn, address = s.accept()
        s.setblocking(1)
        connections.append(conn)
        addresses.append(addresses)

def receive_commands(connections):
    while True:
        for conn in connections:
            data=conn.recv(1024)
            string=str(data[:].decode("utf-8"))
            length=str(len(connections))
            if string=='@TanweerAli#:~' + 'list':
                conn.send(str.encode(length))
            else:
                for i in connections:
                    if i==conn:
                        continue
                    else:
                        i.send(str.encode(string))

def list_connections(connections):
    while True:
        for i,j in enumerate(connections):
            try:
                j.send(str.encode(' '))
                j.recv(20480)
            except:
                del connections[i]
                del addresses[i]
                continue


def work(j):
    if j==0:
        create_socket()
        bind_socket()
        socket_accept()
    elif j==1:
        receive_commands(connections)
    elif j==2:
        list_connections(connections)


for j in range(3):
    t=threading.Thread(target=work, args=(j,))
    t.start()

