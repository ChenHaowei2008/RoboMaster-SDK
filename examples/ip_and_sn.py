# Use an acutally working library lol
from djitellopy import Tello
from subprocess import check_output
import re

# replace 192.168.0.0 with your local wifi subnet.
ips = check_output(["nmap", "-sn", "192.168.0.0-255"]).strip().split(b'\n')
ips = [re.findall(b"((?:\d+\.){3}\d+)", i)[0] for i in ips if b"Nmap scan report for RMTT" in i]
# ten million iq play

# Enter in your robot serial numbers in the order that you want them in.
robot_sn_list = [
     "0TQZK8CCNAAAAA", # drone 1
     "0TQZK88CNAAAAA", # drone 2
     "0TQZK8CCNAAAAA", # drone 3
     "0TQZK4BCNAAAAA", # drone 4
]

ip_sn_dict = {}

def construct_sn_ip(tello, ip):
     global ip_sn_dict
     tello.connect()
     ip_sn_dict.update({tello.query_serial_number(): (ip, 8889)})
     tello.send_command_without_return("downvision 1")
     
for ip in ips:
     tello = Tello(ip.decode())
     construct_sn_ip(tello, ip.decode())

print(ip_sn_dict)

# you can use import ip_sn_dict from ip_and_sn to obtain the vairable automatically.