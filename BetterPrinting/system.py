import datetime
import platform
import os
import getpass
import socket
from .color import color


class system:

    @staticmethod
    def sys_info(**show):
        printable = """"""
        kw = ['all', 'user', 'name', 'os', 'version', 'processor', 'architecture', 'ip']
        sysminf = platform.uname()

        key = str(show.keys()).replace("dict_keys", "").replace("(", "").replace(")", "").replace("'", "").replace("[",
                                                                                                                   "").replace(
            "]", "").replace(" ", "")
        keys = key.split(",")

        if not show == {}:
            for i in keys:
                if i in kw:
                    if "user" in i:
                        printable += ("|" + color("USER: ", "green", print_val=False) + f"{getpass.getuser()}\n")
                    if "name" in i:
                        printable += ("|" + color("NAME: ", "green", print_val=False) + f"{sysminf.node}\n")
                    if "os" in i:
                        printable += ("|" + color("OS: ", "green", print_val=False) + f"{sysminf.system}\n")
                    if "version" in i:
                        printable += ("|" + color("VERSION: ", "green", print_val=False) + f"{sysminf.version}\n")
                    if "processor" in i:
                        printable += ("|" + color("PROCESSOR: ", "green", print_val=False) + f"{sysminf.processor}\n")
                    if "architecture" in i:
                        printable += ("|" + color("ARCHITECTURE: ", "green", print_val=False) + f"{sysminf.machine}\n")
                    if "ip" in i:
                        printable += ("|" + color("IP-ADDRESS: ", "green", print_val=False) + f"{socket.gethostbyname(socket.gethostname())}\n")
                    if "all" in i:
                        printable += ("|" + color("USER: ", "green", print_val=False) + f"{getpass.getuser()}\n")
                        printable += ("|" + color("NAME: ", "green", print_val=False) + f"{sysminf.node}\n")
                        printable += ("|" + color("OS: ", "green", print_val=False) + f"{sysminf.system}\n")
                        printable += ("|" + color("VERSION: ", "green", print_val=False) + f"{sysminf.version}\n")
                        printable += ("|" + color("PROCESSOR: ", "green", print_val=False) + f"{sysminf.processor}\n")
                        printable += ("|" + color("ARCHITECTURE: ", "green", print_val=False) + f"{sysminf.machine}\n")
                        printable += ("|" + color("IP-ADDRESS: ", "green", print_val=False) + f"{socket.gethostbyname(socket.gethostname())}\n")
                else:
                    pass

        else:
            printable += ("|" + color("USER: ", "green", print_val=False) + f"{getpass.getuser()}\n")
            printable += ("|" + color("NAME: ", "green", print_val=False) + f"{sysminf.node}\n")
            printable += ("|" + color("OS: ", "green", print_val=False) + f"{sysminf.system}\n")
            printable += ("|" + color("VERSION: ", "green", print_val=False) + f"{sysminf.version}\n")
            printable += ("|" + color("PROCESSOR: ", "green", print_val=False) + f"{sysminf.processor}\n")
            printable += ("|" + color("ARCHITECTURE: ", "green", print_val=False) + f"{sysminf.machine}\n")
            printable += ("|" + color("IP-ADDRESS: ", "green", print_val=False) + f"{socket.gethostbyname(socket.gethostname())}\n")

        print(printable)

    @staticmethod
    def time(print_val: bool = True, strftime: str = "%H:%M:%S"):
        now_all = datetime.datetime.now()
        now = now_all.strftime(strftime)
        if print_val:
            return print(now)
        else:
            return now

    @staticmethod
    def date(print_val: bool = True, strftime: str = "%d.%m.%G"):
        now_all = datetime.datetime.now()
        now = now_all.strftime(strftime)
        if print_val:
            return print(now)
        else:
            return now

    @staticmethod
    def tasks():
        plat = platform.system()
        if "Windows" in plat:
            os.system("tasklist")
        elif "Linux" in plat:
            os.system("ps aux")
        else:
            print("os not detected")
