def login(logpasswd, password, loguname):
    if(logpasswd == password):
        print("login success")
	import socket
	import threading
	import sys

	s=socket.socket()
	host = 'SERVER's IP ADDRESS'
	port = 5568

	s.connect((host, port))
	print("CONNECTED! USE 'list' COMMAND TO KNOW NUMBER OF USERS ONLINE AND USE 'quit' COMMNAD TO COME OUT OF CHATROOM!")
	
	string = '@' + loguname + '#:~'
	def send_commands():
    		while True:
        		cmd = input("@" + loguname + "#:~ ")
        		if cmd=='quit':
				s.send(str.encode(string + cmd))
            			break
        		else:
            			s.send(str.encode(string + cmd))
		def receive_commands():
    			while True:
        			data = s.recv(1024)
				string = str(data[:].decode("utf-8"))
				if string == "YOU ARE OUT":
					break
        			elif len(data) > 0:
            				print(string)
			print(string)

	t1=threading.Thread(target=send_commands)
	t2=threading.Thread(target=receive_commands)

	t1.start()
	t2.start()
	
	t1.join()
	t2.join()

	sys.exit(0)
    else:
        print("Invalid Password")
loguname = input("Enter Username: ")
logpasswd = input("Enter password: ")

import mysql.connector
mydb = mysql.connector.connect(host="IP_address_of_database_server_here", user="root", passwd="P@$$w0rd", database="login")
mycursor = mydb.cursor()
mycursor.execute("SELECT AES_DECRYPT(password, 'tanweer_ali') FROM credentials WHERE username='%s'" % loguname)
for i in mycursor:
    a=i[0]
    b=a.decode('utf-8')
try:
    login(logpasswd, b, loguname)
except NameError:
    print("Invalid Username")
