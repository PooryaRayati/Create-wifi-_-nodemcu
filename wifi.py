import network
import socket
#network
ap = network.WLAN(network.AP_IF)
ap.config(essid="POORYA_IOT",password="10281387")
ap.active(True)

print("wifi created!")
print(ap.ifconfig())

#socket
socket_ap = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket_ap.bind(("192.168.4.1", 80 ))
socket_ap.listen(1)

#send and receive data
client_ap = socket_ap.accept()
print(client_ap{0})
client_ap{0}.send("hello !!")
