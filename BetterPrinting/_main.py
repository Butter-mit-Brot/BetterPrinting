from termcolor import colored
import platform
import os


def multi_lines(*args):
    print("\n".join(args))


def break_line(amount=20):
    print("-" * amount)


def color(text, color, print_val=True):
    if print_val is True:
        return print(colored(text, color))
    elif print_val is False:
        return colored(text, color)
    else:
        raise TypeError("print_val must be a bool!")


def clear():
    plat = platform.system()
    if "Windows" in plat:
        os.system("cls")
    elif "Linux" in plat:
        os.system("clear")
    else:
        print("os not detected")


def split_wrd(text, print_val=True):
    txt = text
    sp = txt.split(" ")
    if print_val is True:
        return print(sp)
    elif print_val is False:
        return sp
    else:
        raise TypeError("print_val must be a bool!")


def multi_input(number):
    lines = []
    for i in range(number):
        lines.append(input())
    return lines
