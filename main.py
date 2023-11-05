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
]

while True:
    cmd = input(f"{cyan}{user}{host} {green}${reset} ")
    cmd = cmd.split(" ", 1)
    if cmd[0] == "help":
        if len(cmd) == 1:
            print("Available commands: ")
            for item in available:
                print(f"{white}{item['name']}{reset} -> {item['desc']}")
            print("\nType \"help -i\" to see the information of this app")
        elif len(cmd) == 2 and cmd[1] == "-i":
        	print(info)
    elif cmd[0] == "clear":
        clear()
    elif cmd[0] == "echo":
        if len(cmd) == 2:
            print(cmd[1])
        else:
            print(f"{yellow}Please input the parameter.{reset} e.g : echo hello")
    elif cmd[0] == "ls":
        ls()
    elif cmd[0] == "pwd":
        system("pwd")
    elif cmd[0] == "ascii":
        if len(cmd) == 2:
            print(text2art(cmd[1]))
        else:
            print(f"{yellow}Please input the parameter.{reset} e.g : ascii hello")
    elif cmd[0] == "sysinfo":
        print("Operating System: ", platform.system())
        print("Platform: ", platform.platform())
        print("Machine: ", platform.machine())
        print("Node Name: ", platform.node())
        print("Python: ", platform.python_version())
    elif cmd[0] == "api":
        if len(cmd) == 2:
            try:
                res = req.get(cmd[1])
                res = res.json()
                print(res)
            except:
                print(
                    f"{yellow}Error when doing http request. Please check your internet connection or the url you typed. The url may be invalid or the referenced url is not available or it does not provide any response{white}"
                )
                continue
        else:
            print(f"{yellow}Please input the url.{reset} e.g : api https://example.com")
    else:
        print(f'{yellow}Command not found.{reset} Run "help" to see listed commands')
        
        
# 100 hundred lines :-)