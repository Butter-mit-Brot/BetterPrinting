import platform
import os


def multi_lines(*args):
    print("\n".join(args))


def break_line(amount: int = 20):
    print("-"*amount)


def break_down(amount: int):
    print("\n"*amount)


def clear(platformic: bool = True):
    plat = platform.system()
    if platformic:
        if "Windows" in plat:
            os.system("cls")
        elif "Linux" in plat:
            os.system("clear")
        else:
            print("\n" * 100)
    else:
        print("\n" * 100)


def split_wrd(text: str, print_val: bool = True):
    txt = text
    sp = txt.split(" ")
    if print_val:
        return print(sp)
    else:
        return sp


def multi_input(number: int, prompt=""):
    lines = []
    for i in range(number):
        lines.append(input(prompt))
    return lines
