import os

def scan_network():
  ip_list = []
  for i in range(1,256):
    ip = "192.168.20."+str(i)
    response = os.system("ping -c 1 " + ip)
    if response == 0:
      ip_list.append(ip)
  return ip_list

ip_list = scan_network()
print(ip_list)
