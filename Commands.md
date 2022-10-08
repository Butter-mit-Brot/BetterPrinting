**every function that puts out data/strings has a print_val bool that is automaticly set to true and instant prints, if set to false you can use the return value**

# Main functions

**multi_lines** (multiple Lines)[prints out multiple Lines]    _BetterPrinting.multiLines("text", "text and more")_

**break_line** [prints a Line with minuses]     _BetterPrinting.breakline({optional}amount=number)_

**clear** [clears your terminal(windows/linux)]     _BetterPrinting.clear()_

**split_wrd** (split word)[makes a big text to an list of words]    _BetterPrinting.splitWRD("Splits the text if space is between the words", print_val)_

**multi_input** [lets you get multiple inputs at ones (returns a list so you have a index of your inputs)]     _BetterPrinting.multi_input(number of lines)_

## color

**color** [puts out a colored version of your text]    _BetterPrinting.color("text", "color for example red", print_val)_

**rainbow_text** [makes your string a rainbow :)]     _BetterPrinting.rainbow_text("text", print_val)_

## random

**random_str** (random string)[prints out a random String of letters, numbers and special characters]    _BetterPrinting.randmSTR(number, print_val)_

**random_ltr** (random letters)[prints out a random combination of letters]    _BetterPrinting.randmLTR(number, print_val)_

**random_dig** (random digits)[prints out a random combination of numbers]    _BetterPrinting.randmDIG(number, print_val)_

**random_sym** (random symbols)[prints out a random combination of special characters]    _BetterPrinting.randmSYM(number, print_val)_

# class draw:

**draw** [inits the class]    _var_name = BetterPrinting.draw(canvas size x, canvas size y, {optional character to be used for drawing})_

**var_name.set_pos** [sets position of pencil]    _var_name.set_pos(x, y)_

**var_name.forward** [goes forward an specific amount of characters in set direction]    _var_name.forward(distance)_

**var_name.turn** [turns you into set direction (does not draw)]    _var_name.turn(direction[You can only use "right", "left", "down", "up"])_

**turn_reset** [resets direction to right]    _var_name.turn_reset()_

**done** [draws the canvas]    _var_name.done()_

# class system:

**sys_info** (systeminfo)[prints systeminfo]     _BetterPrinting.system.sysinfo({leave empty if everything should be shown or write all=True} {if you just want to show specific information write the keywords + = + True for example: user=True} all keywords: user, name, os, version, processor, architecture, ip)_

**time** [prints or returns the time]     _BetterPrinting.system.time(print_val)_

**date** [prints or returns the date]     _BetterPrinting.system.date(print_val)_

**tasks** [prints out the current tasks (works only in windows and Linux)]     _BetterPrinting.system.tasks()_

# class ui:

**title_bar** [prints a title bar with a text]     _BetterPrinting.ui.title_bar(Title, {optional}spaces=number of spaces)_

**text_box** [prints a text box with any amount of text]     _BetterPrinting.ui.text_box(text, text, text {any amount}, {optional}free_line = even number, {optional}rounded_edges= True or False)_

**list** [Prints a list the fancy way]     _BetterPrinting.ui.list(list, name{what name you give your list})_

**number** [Prints a easy to use Option selector screen]     _BetterPrinting.ui.number(all strings, {optional}break_line=True or False)_

**ascii_label** [Print a label next to your ascii art]     _BetterPrinting.ui.ascii_label(the art, the label, in wich row, {optional}space= the space between text and art)_
