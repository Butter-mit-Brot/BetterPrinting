import time
import platform
import os


class ui:

    @staticmethod
    def title_bar(title: str, spaces: int = 0):
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
            print("|" + " " * space + title + " " * space + " |")
        else:
            print("|" + " " * space + title + " " * space + "|")
        print("|" + "-" * multi + "|")

    @staticmethod
    def text_box(*text: str, free_line: int = 2, rounded_edges: bool = False):
        longest = max(text, key=len)  # get the longest argument
        leng = len(longest)
        multi = int(leng) * 2  # get the length times two so we can work with a nice box

        free = free_line // 2

        ###################### print the beginning
        if not rounded_edges:
            print("|" + "-" * multi + "|")
        else:
            print("/" + "-" * multi + "\\")

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
        if not rounded_edges:
            print("|" + "-" * multi + "|")
        else:
            print("\\" + "-" * multi + "/")

    @staticmethod
    def list(lst: list, list_name):
        n_lst = [str(i) for i in lst]
        longest = max(n_lst, key=len)

        if len(list_name) > len(longest):
            long = len(list_name) + 1
        else:
            long = len(longest) + 1

        space = (long - len(list_name)) // 2
        if space == 0:
            if len(list_name) % 2:
                print("|" + " " * space + list_name + " " * space + " |")
            else:
                print("|" + " " * space + list_name + " " * space + " |")
        else:
            if len(list_name) % 2:
                print("|" + " " * space + list_name + " " * space + " |")
            else:
                print("|" + " " * space + list_name + " " * space + "|")

        for word in n_lst:
            space2 = long - len(word)
            print("|" + "-" * long + "|")
            print("|" + word + " " * space2 + "|")
        print("|" + "-" * long + "|")

    @staticmethod
    def number(*lines, break_line: bool = True):
        n_lst = [str(i) for i in lines]
        longest = max(n_lst, key=len)
        long = len(longest) + 5

        if break_line:
            print("-" * long)
        for i in range(1, len(lines) + 1):
            print(f"[{i}] {lines[i - 1]}")
        if break_line:
            print("-" * long)

    @staticmethod
    def ascii_label(image: str, text: str, row: int, space: int = 5):
        map = []
        for i in image.splitlines():
            map.append(i)

        lines = len(map)
        if row > lines:
            raise TypeError(f"Row can't be bigger then the number of lines({lines}) in your image")

        longest = max(map, key=len)
        lon = len(longest)
        num = 0
        for i in map:
            num += 1
            s = lon - len(i)
            sks = s + space
            if num == row:
                print(i + " " * sks + text)
            else:
                print(i + " " * sks)


# This is still in Beta(I don't really know what to make with it):

class animation:

    @staticmethod
    def string_change(string1, string2, sleep=0.5, os_clear: bool = True):
        if os_clear:
            plat = platform.system()
            if "Windows" in plat:
                clear = "win"
            elif "Linux" in plat:
                clear = "linux"
            else:
                print("os not detected")
        else:
            clear = "down"

        l1 = len(string1)
        l2 = len(string2)

        for i in range(l1 + 1):
            s1 = string1
            print(s1, end="")
            k = int(l2) - i
            print("\b" * i, string2 + "\b" * k)
            time.sleep(sleep)
            if clear == "win":
                os.system("cls")
            elif clear == "Linux":
                os.system("clear")
            else:
                print("\n" * 500)
        print(string2)
