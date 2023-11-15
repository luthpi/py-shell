from colorama import Fore
from os import name, system
from art import text2art
import platform
import requests as req
import json

info = """
   Python Shell 
   Made by Luthpai
   GitHub : @luthpai
   This is just for fun.
   Thanks for using :)
   
   License : MIT License
"""

class CMD:
	def clear():
		if name == "nt":
			system("cls")
		else:
			system("clear")
	
	def ls():
		if name == "nt":
			system("dir")
		else:
			system("ls")
			
	def cd(dir):
		system(f"cd {dir}")
		
	def fetch(url):
		try:
		    res = req.get(url)
		    res = res.json()
		    print(res)
		except:
		        print(
                f"{yellow}Error while doing http request. Please check your internet connection or the url you typed. The url might be invalid or the referenced url is not available or it does not provide any response{white}"
            )
            
	def sysinfo():
	   print("Operating System: ", platform.system())
	   print("Platform: ", platform.platform())
	   print("Machine: ", platform.machine())
	   print("Node Name: ", platform.node())
	   print("Python: ", platform.python_version())
			
cmd = CMD

cyan = Fore.CYAN
green = Fore.GREEN
white = Fore.WHITE
yellow = Fore.YELLOW
reset = Fore.RESET

user = "py-shell"
host = "@" + platform.node()
available = [
    {"name": "echo", "desc": "print out text to console"},
    {"name": "clear", "desc": "clear console"},
    {"name": "ls", "desc": "print out what inside current directory"},
    {"name": "pwd", "desc": "print out what is the current directory"},
    {"name": "ascii", "desc": "transform normal text to ascii"},
    {"name": "sysinfo", "desc": "print out user's device information"},
    {"name": "api", "desc": "simply get the json response from an api"},
    {"name": "cd", "desc": "change directory"}
]

while True:
    inp = input(f"{cyan}{user}{host} {green}${reset} ")
    inp = inp.split(" ", 1)
    if inp[0] == "help":
        if len(inp) == 1:
            print("Available commands: ")
            for item in available:
                print(f"{white}{item['name']}{reset} -> {item['desc']}")
            print("\nType \"help -i\" to see the information of this app")
        elif len(inp) == 2 and inp[1] == "-i":
        	print(info)
    elif inp[0] == "clear":
        cmd.clear()
    elif inp[0] == "echo":
        if len(inp) == 2:
            print(inp[1])
        else:
            print(f"{yellow}Please input the parameter.{reset} e.g : echo hello")
    elif inp[0] == "ls":
        cmd.ls()
    elif inp[0] == "pwd":
        system("pwd")
    elif inp[0] == "ascii":
        if len(inp) == 2:
            print(text2art(inp[1]))
        else:
            print(f"{yellow}Please input the parameter.{reset} e.g : ascii hello")
    elif inp[0] == "sysinfo":
        cmd.sysinfo()
    elif inp[0] == "api":
        if len(inp) == 2:
            cmd.fetch(inp[1])
            continue
        else:
            print(f"{yellow}Please input the url.{reset} e.g : api https://example.com")
    elif inp[0] == "cd":
    	if len(inp) == 2:
    		cmd.cd(inp[1])
    	else:
    		print(f"{yellow}Invalid. {white}Please input the directory you want to go to.")
    else:
        print(f'{yellow}Command not found.{reset} Run "help" to see listed commands')