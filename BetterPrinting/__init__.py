from termcolor import colored
import random
import string

def oneLine(text1L):
    print(text1L)

def twoLine(text2L, text2L2):
    print(text2L, "\n" + text2L2)

def threeLine(text3L, text3L2, text3L3):
    print(text3L, "\n" + text3L2 + "\n" + text3L3)

def color(text, color):
    print(colored(text, color))

def splitWRD(text):
    txt = text
    print(txt.split(","))

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

