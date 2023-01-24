import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.setdefaulttimeout(1)
#Si el puerto esta abierto es igual a 0.
#Si el puerto esta cerrado es igual a 111. 
result = s.connect_ex(('192.168.20.110',22))
print(result)
