from termcolor import colored
import random
import string
import os

def printLines(*args):
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


def creatF(name, text):

    def _select_mode(file):
        """
        Checks if file exists and if file is empty.
        Based on these factors returns file mode.
        """
        if os.path.isfile(name):

            if os.stat(name).st_size != 0:
                return 'a'
            return 'w'
        
        return 'x'
    
    # If file already exists and is not empty, this file will be opened in 'a' (append) mode
    # If file already exists and is empty, this file will be opened in 'w' (write) mode
    # If file does not exist, this file will be created by open() function and will e opened in 'x' mode

    # The difference between 'a' mode and 'w' mode is that when file is opned in 'a' mode, the content is 
    # simply appended to the end of the file
    # When file is opened in 'w' mode, ALL FILE'S CONTENT WILL BE OVERWRITTEN by new one.

    # _select_mode() function is responsible for checking and selecting appropriate file modes

    f = open(name, _select_mode(name))
    # By default there is no newline appended. 
    f.write(text + '\n')
    f.close()
