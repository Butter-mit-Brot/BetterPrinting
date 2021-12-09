import datetime
import platform
import os
import getpass
import socket
from .color import color


class system:

    @staticmethod
    def sys_info(**show):
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
                        print("|" + color("USER: ", "green", print_val=False) + f"{getpass.getuser()}")
                    if "name" in i:
                        print("|" + color("NAME: ", "green", print_val=False) + f"{sysminf.node}")
                    if "os" in i:
                        print("|" + color("OS: ", "green", print_val=False) + f"{sysminf.system}")
                    if "version" in i:
                        print("|" + color("VERSION: ", "green", print_val=False) + f"{sysminf.version}")
                    if "processor" in i:
                        print("|" + color("PROCESSOR: ", "green", print_val=False) + f"{sysminf.processor}")
                    if "architecture" in i:
                        print("|" + color("ARCHITECTURE: ", "green", print_val=False) + f"{sysminf.machine}")
                    if "ip" in i:
                        print("|" + color("IP-ADDRESS: ", "green", print_val=False) + f"{socket.gethostbyname(socket.gethostname())}")
                    if "all" in i:
                        print("|" + color("USER: ", "green", print_val=False) + f"{getpass.getuser()}")
                        print("|" + color("NAME: ", "green", print_val=False) + f"{sysminf.node}")
                        print("|" + color("OS: ", "green", print_val=False) + f"{sysminf.system}")
                        print("|" + color("VERSION: ", "green", print_val=False) + f"{sysminf.version}")
                        print("|" + color("PROCESSOR: ", "green", print_val=False) + f"{sysminf.processor}")
                        print("|" + color("ARCHITECTURE: ", "green", print_val=False) + f"{sysminf.machine}")
                        print("|" + color("IP-ADDRESS: ", "green", print_val=False) + f"{socket.gethostbyname(socket.gethostname())}")
                else:
                    pass

        elif show == {}:
            print("|" + color("USER: ", "green", print_val=False) + f"{getpass.getuser()}")
            print("|" + color("NAME: ", "green", print_val=False) + f"{sysminf.node}")
            print("|" + color("OS: ", "green", print_val=False) + f"{sysminf.system}")
            print("|" + color("VERSION: ", "green", print_val=False) + f"{sysminf.version}")
            print("|" + color("PROCESSOR: ", "green", print_val=False) + f"{sysminf.processor}")
            print("|" + color("ARCHITECTURE: ", "green", print_val=False) + f"{sysminf.machine}")
            print("|" + color("IP-ADDRESS: ", "green", print_val=False) + f"{socket.gethostbyname(socket.gethostname())}")

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
