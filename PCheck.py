# Port Checker By AliReza. @NetworkSide
from requests import post , get
from os import system as run
from colorama import Fore as c
from time import sleep as s

run("clear" or "cls")

IP = input(c.RED + "[IP]" + c.WHITE + ": " + c.GREEN + "Please Enter Target Address ~> " + c.RESET )

if IP.lower() == 'myip':
	print(c.BLUE + "Getting Your IP...",end='\r')
	IP = get("https://api.ipify.org/").text
	print(c.BLUE + "Getting Your IP..." + c.YELLOW + " OK")
	print(c.BLUE + "Your Internet IP: "+ c.YELLOW + IP + c.RESET)

type = int(input(c.GREEN + "[1]" + c.WHITE + ":" + c.YELLOW + " Check One Port" + c.CYAN + " @ " + c.GREEN + "[2]" + c.WHITE + ":" + c.YELLOW + " Check Range Of Ports" + c.RESET + " ~# "))
if type == 1:
	Port = input(c.RED + "[PORT]" + c.WHITE + ": " + c.GREEN + "Please Enter Port Number ~> " + c.RESET )

	data = {'remoteAddress':IP , 'portNumber':Port}
	print(c.BLUE + "Sending Data To Server ...",end='\r')
	r = post("https://ports.yougetsignal.com/check-port.php" , data=data)
	print(c.BLUE + "Sending Data To Server..." + c.YELLOW + " OK")
	print(c.BLUE + "Checking port is open..." , end='\r')
	s(2)
	print(c.BLUE + "Checking port is open... " + c.YELLOW + "OK")
	print(c.BLUE + "Getting result from server..." , end='\r' + c.RESET)
	s(1.4)
	print(c.BLUE + "Getting result from server... " + c.YELLOW + "OK" + c.RESET)
	if "closed" in r.text:
		print(f"Port {Port} is " + c.RED + "closed" + c.RESET + f" on {IP}")
	if "open" in r.text:
		print(f"Port {Port} is " + c.GREEN + "opened" + c.RESET + f" on {IP}")
if type == 2:
	fromx = int(input(c.BLUE + "From ~> "+ c.RESET))
	toy = int(input(c.BLUE + "To ~> "+ c.RESET))
	for port in range(fromx , toy + 1):
		data = {'remoteAddress':IP , 'portNumber':port}
		r = post("https://ports.yougetsignal.com/check-port.php" , data=data)
		if "closed" in r.text:
			print(f"Port {port} is " + c.RED + "closed" + c.RESET + f" on {IP}")
		if "open" in r.text:
			print(f"Port {port} is " + c.GREEN + "opened" + c.RESET + f" on {IP}")
