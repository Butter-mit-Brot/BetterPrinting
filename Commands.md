**every function that puts out data/strings has a print_val bool that is automaticly set to true and instant prints, if set to false you can use the return value**

# Main functions

**multi_lines** (multiple Lines)[prints out multiple Lines]    _BetterPrinting.multiLines("text", "text and more")_

**break_line** [prints a Line with minuses]     _BetterPrinting.breakline({optional}amount=number)_

**clear** [clears your terminal(windows/linux)]     _BetterPrinting.clear()_

**split_wrd** (split word)[makes a big text to an list of words]    _BetterPrinting.splitWRD("Splits the text if space is between the words", print_val)_

## color

**color** [puts out a colored version of your text]    _BetterPrinting.color("text", "color for example red", print_val)_

**rainbow_text** [makes your string a rainbow :)]     _BetterPrinting.rainbow_text("text", print_val)_

## random

**random_str** (random string)[prints out a random String of letters, numbers and special characters]    _BetterPrinting.randmSTR(number, print_val)_

**random_ltr** (random letters)[prints out a random combination of letters]    _BetterPrinting.randmLTR(number, print_val)_

**random_dig** (random digits)[prints out a random combination of numbers]    _BetterPrinting.randmDIG(number, print_val)_

**random_sym** (random symbols)[prints out a random combination of special characters]    _BetterPrinting.randmSYM(number, print_val)_

# class system:

**sys_info** (systeminfo)[prints systeminfo]     _BetterPrinting.system.sysinfo({leave empty if everything should be shown or write all=True} {if you just want to show specific information write the keywords + = + True for example: user=True} all keywords: user, name, os, version, processor, architecture, ip)_

**time** [prints or returns the time]     _BetterPrinting.system.time(print_val)_

**date** [prints or returns the date]     _BetterPrinting.system.date(print_val)_

**tasks** [prints out the current tasks (works only in windows and Linux)]     _BetterPrinting.system.tasks()_

### class ui:

**title_bar** [prints a title bar with a text]     _BetterPrinting.ui.title_bar(Title, {optional}spaces=number of spaces)_

**text_box** [prints a text box with any amount of text]     _BetterPrinting.ui.text_box(text, text, text {any amount}, {optional}free_line = even number, {optional}rounded_edges= True or False)_
