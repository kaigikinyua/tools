import socket
import threading
class Server:
    clientlist=[]
    #get ip of the hostmachine and port
    def __init__(self):
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
            s.bind((socket.gethostname(),5000))
            print("Server running on port 5000")
            s.listen()
            i=0
            while i<10:
                conn,addr=s.accept()
                t=threading.Thread(target=self.connect,name="client",args=(conn,))
                t.start()
                i+=1
        except:
            print("Error while binding to socket")
    def connect(self,conn):
        print(conn)
        print("Connected")
    def recvmessage(self):
        pass
    #pass a message from one client to the next
    def channel(self,sender,receiver):
        pass 
s=Server()