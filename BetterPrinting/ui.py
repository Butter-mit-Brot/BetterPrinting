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
            print("|" + " " * space + title + " " * space + " |")
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
