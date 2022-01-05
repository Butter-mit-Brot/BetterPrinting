from .color_list import *


def color(text, color, print_val: bool = True):
    if color not in c_lst:
        raise TypeError(f"{color} is not a supported color!")

    col = c_dict[color] + text + c_dict["stop"]

    if print_val:
        return print(col)
    else:
        return col


def rainbow_text(text, print_val: bool = True):
    row = ["red", "blue", "green", "cyan", "yellow", "magenta"]
    col_var = 0
    out = ""
    for i in text:
        if col_var == 6:
            col_var = 0
        out += c_dict[row[col_var]] + i + c_dict["stop"]
        col_var += 1

    if print_val:
        return print(out)
    else:
        return out
