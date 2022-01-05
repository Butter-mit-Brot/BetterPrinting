import random
import string


def random_str(length, print_val: bool = True):
    l = string.printable
    str = ''.join(random.choice(l) for i in range(length))
    if print_val:
        return print(str)
    else:
        return str


def random_ltr(length, print_val: bool = True):
    l = string.ascii_letters
    str = ''.join(random.choice(l) for i in range(length))
    if print_val:
        return print(str)
    else:
        return str


def random_dig(length, print_val: bool = True):
    l = string.digits
    str = ''.join(random.choice(l) for i in range(length))
    if print_val:
        return print(str)
    else:
        return str


def random_sym(length, print_val: bool = True):
    l = string.punctuation
    str = ''.join(random.choice(l) for i in range(length))
    if print_val:
        return print(str)
    else:
        return str
