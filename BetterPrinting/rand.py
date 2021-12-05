import random
import string


def random_str(length, print_val=True):
    l = string.printable
    str = ''.join(random.choice(l) for i in range(length))
    if print_val is True:
        return print(str)
    elif print_val is False:
        return str
    else:
        raise TypeError("print_val must be a bool!")


def random_ltr(length, print_val=True):
    l = string.ascii_letters
    str = ''.join(random.choice(l) for i in range(length))
    if print_val is True:
        return print(str)
    elif print_val is False:
        return str
    else:
        raise TypeError("print_val must be a bool!")


def random_dig(length, print_val=True):
    l = string.digits
    str = ''.join(random.choice(l) for i in range(length))
    if print_val is True:
        return print(str)
    elif print_val is False:
        return str
    else:
        raise TypeError("print_val must be a bool!")


def random_sym(length, print_val=True):
    l = string.punctuation
    str = ''.join(random.choice(l) for i in range(length))
    if print_val is True:
        return print(str)
    elif print_val is False:
        return str
    else:
        raise TypeError("print_val must be a bool!")
