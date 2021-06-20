from termcolor import colored
import random
import string
import os


def multiLines(*args):
    print("\n".join(args))

def color(text, color):
    print(colored(text, color))

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

def createF(name, text, overwrite=False):
    def _select_mode(file):
        # Thanks to NickolaiBeloguzov for helping me with the os path function!
        if os.path.isfile(name):

            if os.stat(name).st_size != 0:
                if overwrite == False:
                    return 'a'
                else:
                    pass
            return 'w'

        return 'x'
    f = open(name, _select_mode(name))
    f.write(text + '\n')
    f.close()