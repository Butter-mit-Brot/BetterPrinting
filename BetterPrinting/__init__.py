from termcolor import colored
import random
import string
import datetime
import platform
import os
import getpass
import socket


# added multInput, ui
# added print_val to all functions that pass out data for example randmSTR or splitWRD

def multiLines(*args):
    print("\n".join(args))


def breakline(amount=20):
    print("-" * amount)


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


def splitWRD(text, print_val=True):
    txt = text
    sp = txt.split(" ")
    if print_val is True:
        return print(sp)
    elif print_val is False:
        return sp
    else:
        raise TypeError("print_val must be a bool!")


# random functions

def randmSTR(length, print_val=True):
    l = string.printable
    str = ''.join(random.choice(l) for i in range(length))
    if print_val is True:
        return print(str)
    elif print_val is False:
        return str
    else:
        raise TypeError("print_val must be a bool!")


def randmLTR(length, print_val=True):
    l = string.ascii_letters
    str = ''.join(random.choice(l) for i in range(length))
    if print_val is True:
        return print(str)
    elif print_val is False:
        return str
    else:
        raise TypeError("print_val must be a bool!")


def randmDIG(length, print_val=True):
    l = string.digits
    str = ''.join(random.choice(l) for i in range(length))
    if print_val is True:
        return print(str)
    elif print_val is False:
        return str
    else:
        raise TypeError("print_val must be a bool!")


def randmSYM(length, print_val=True):
    l = string.punctuation
    str = ''.join(random.choice(l) for i in range(length))
    if print_val is True:
        return print(str)
    elif print_val is False:
        return str
    else:
        raise TypeError("print_val must be a bool!")


# Input

def multInput(number):
    lines = []
    for i in range(number):
        lines.append(input())
    return lines


################################################################### system class
class system:

    @staticmethod
    def sysinfo(**show):
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


################################################################### ui class
class ui:

    @staticmethod
    def title_bar(title: str, spaces=0):
        if "\n" in title:
            raise TypeError("\\n is not allowed in the title bar")

        leng = len(title)
        if spaces == 0:
            multi = leng * 2
            space = multi // 4
        else:
            multi = leng + spaces * 2
            space = spaces

        print("|" + "-" * multi + "|")
        if leng % 2:
            print("|" + " " * space + title + " " * space + "|")
        else:
            print("|" + " " * space + title + " " * space + "|")
        print("|" + "-" * multi + "|")

    @staticmethod
    def text_box(*text: str, free_line=2, rounded_edges=False):
        longest = max(text, key=len)  # get the longest argument
        leng = len(longest)
        multi = int(leng) * 2  # get the length times two so we can work with a nice box

        free = free_line // 2

        ###################### print the beginning
        if rounded_edges is False:
            print("|" + "-" * multi + "|")
        elif rounded_edges is True:
            print("/" + "-" * multi + "\\")
        else:
            raise TypeError("rounded_edges must be a bool!")

        for i in range(free):
            print(("|" + " " * multi + "|"))
        ######################

        for tex in text:

            if "\n" in tex:
                raise TypeError("\\n is not allowed in string make two separate strings instead")

            tex_len = len(tex)
            if tex == longest:
                four = multi // 4
                if leng % 2:
                    print("|" + " " * four + tex + " " * four + " |")
                else:
                    print("|" + " " * four + tex + " " * four + "|")
            else:
                mult = multi - len(tex)
                two = mult // 2
                if tex_len % 2:
                    print("|" + " " * two + tex + " " * two + " |")
                else:
                    print("|" + " " * two + tex + " " * two + "|")

        #####################    print the end
        for i in range(free):
            print(("|" + " " * multi + "|"))
        if rounded_edges is False:
            print("|" + "-" * multi + "|")
        elif rounded_edges is True:
            print("\\" + "-" * multi + "/")
        else:
            raise TypeError("rounded_edges must be a bool!")
