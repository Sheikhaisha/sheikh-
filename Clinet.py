import sockets
 
PORT = 5050
 server ='localhost'
 ADDR = (server,port)
 FORMATE ="utf-8"
 DISCONNECT_MESSAGE = "disconnect"

def connectnneCT()c
client = socket.socket(socket.AF_INET,socket.sock_stream)
client.connect(ADDR)
return client

def sent(client, meg)
_______message = msg.encode(utf 8)
client.sent(msg)
client = connect()
sent(client,"testing")
