from termcolor import colored
import random
import string
import datetime
import platform
import os
import getpass
import socket


def multiLines(*args):
    print("\n".join(args))

def breakline(amount=20):
    print("-"*amount)

def color(text, color):
    print(colored(text, color))

def clear():
    plat = platform.system()
    if "Windows" in plat:
        os.system("cls")
    elif "Linux" in plat:
        os.system("clear")
    else:
        print("os not detected")

def splitWRD(text):
    txt = text
    print(txt.split(" "))

def randmSTR(length):
    l = string.printable
    str = ''.join(random.choice(l) for i in range(length))
    print(str)

def randmLTR(length):
    l = string.ascii_letters
    str = ''.join(random.choice(l) for i in range(length))
    print(str)

def randmDIG(length):
    l = string.digits
    str = ''.join(random.choice(l) for i in range(length))
    print(str)

def randmSYM(length):
    l = string.punctuation
    str = ''.join(random.choice(l) for i in range(length))
    print(str)


class system:

    @staticmethod
    def sysinfo(**show):
        kw = ['all', 'user', 'name', 'os', 'version', 'processor', 'architecture', 'ip']
        sysminf = platform.uname()

        key = str(show.keys()).replace("dict_keys", "").replace("(", "").replace(")", "").replace("'", "").replace("[", ""). replace("]", "").replace(" ", "")
        keys = key.split(",")

        if not show == {}:
            for i in keys:
                if i in kw:
                    if "user" in i:
                        print("|" + colored("USER: ", "green") + f"{getpass.getuser()}")
                    if "name" in i:
                        print("|" + colored("NAME: ", "green") + f"{sysminf.node}")
                    if "os" in i:
                        print("|" + colored("OS: ", "green") + f"{sysminf.system}")
                    if "version" in i:
                        print("|" + colored("VERSION: ", "green") + f"{sysminf.version}")
                    if "processor" in i:
                        print("|" + colored("PROCESSOR: ", "green") + f"{sysminf.processor}")
                    if "architecture" in i:
                        print("|" + colored("ARCHITECTURE: ", "green") + f"{sysminf.machine}")
                    if "ip" in i:
                        print("|" + colored("IP-ADDRESS: ", "green") + f"{socket.gethostbyname(socket.gethostname())}")
                    if "all" in i:
                        print("|" + colored("USER: ", "green") + f"{getpass.getuser()}")
                        print("|" + colored("NAME: ", "green") + f"{sysminf.node}")
                        print("|" + colored("OS: ", "green") + f"{sysminf.system}")
                        print("|" + colored("VERSION: ", "green") + f"{sysminf.version}")
                        print("|" + colored("PROCESSOR: ", "green") + f"{sysminf.processor}")
                        print("|" + colored("ARCHITECTURE: ", "green") + f"{sysminf.machine}")
                        print("|" + colored("IP-ADDRESS: ", "green") + f"{socket.gethostbyname(socket.gethostname())}")
                else:
                    pass

        elif show == {}:
            print("|" + colored("USER: ", "green") + f"{getpass.getuser()}")
            print("|" + colored("NAME: ", "green") + f"{sysminf.node}")
            print("|" + colored("OS: ", "green") + f"{sysminf.system}")
            print("|" + colored("VERSION: ", "green") + f"{sysminf.version}")
            print("|" + colored("PROCESSOR: ", "green") + f"{sysminf.processor}")
            print("|" + colored("ARCHITECTURE: ", "green") + f"{sysminf.machine}")
            print("|" + colored("IP-ADDRESS: ", "green") + f"{socket.gethostbyname(socket.gethostname())}")

    @staticmethod
    def time(print_val=True):
        now_all = datetime.datetime.now()
        now = now_all.strftime("%H:%M:%S")
        if print_val is True:
            return print(now)
        elif print_val is False:
            return now
        else:
            raise TypeError("print_val must be a bool!")

    @staticmethod
    def date(print_val=True):
        now_all = datetime.datetime.now()
        now = now_all.strftime("%d.%m.%G")
        if print_val is True:
            return print(now)
        elif print_val is False:
            return now
        else:
            raise TypeError("print_val must be a bool!")

    @staticmethod
    def tasks():
        plat = platform.system()
        if "Windows" in plat:
            os.system("tasklist")
        elif "Linux" in plat:
            os.system("ps aux")
        else:
            print("os not detected")

