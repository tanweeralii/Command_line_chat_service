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
        connections.append(conn)
        addresses.append(addresses)

def receive_commands():
    while True:
        for i,j in enumerate(connections):
            try:
                j.send(str.encode(''))
                j.recv(20480)
            except:
                del connections[i]
                del addresses[i]
                continue
        for i,conn in enumerate(connections):
            data = conn.recv(1024)
            string=str(data[:].decode("utf-8"))
            loguname = string.split('@')
            log = loguname[1]
            log1 = log.split('#')
            log2 = log1[0]
            if string == '@' + log2 + '#:~ ' + 'list':
                conn.send(str.encode(str(len(connections)))
            elif string == '@' + log2 + '#:~ ' + 'quit':
                 send(str.encode("YOU ARE OUT"))  conn.
                 conn.close()
                 del connections[i]
                 del addresses[i]
            else:
                for i in connections:
                    if i==conn:
                        continue
                    else:
                        i.send(str.encode(string)
                               
def work(j):
    if j==0:
        create_socket()
        bind_socket()
        socket_accept()
    elif j==1:
        receive_commands()

for j in range(2):
    t=threading.Thread(target=work, args=(j,))
    t.start()

