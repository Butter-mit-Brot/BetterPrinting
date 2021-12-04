### Main functions

**multiLines** (multiple Lines)[prints out multiple Lines]    _BetterPrinting.multiLines("text", "text and more")_

**breakline** [prints a Line with minuses]     _BetterPrinting.breakline({optional}amount=number)

**color** [puts out a colored version of your text]    _BetterPrinting.color("text", "color for example red")_

**splitWRD** (split word)[makes a big text to an list of words]    _BetterPrinting.splitWRD("Splits the text if space is between the words")_

**randmSTR** (random string)[prints out a random String of letters, numbers and special characters]    _BetterPrinting.randmSTR(number)_

**randmLTR** (random letters)[prints out a random combination of letters]    _BetterPrinting.randmLTR(number)_

**randmDIG** (random digits)[prints out a random combination of numbers]    _BetterPrinting.randmDIG(number)_

**randmSYM** (random symbols)[prints out a random combination of special characters]    _BetterPrinting.randmSYM(number)_

### class system:

**sysinfo** (systeminfo)[prints systeminfo]     _BetterPrinting.system.sysinfo({leave empty if everything should be shown or write all=True} {if you just want to show specific information write the keywords + = + True for example: user=True} all keywords: user, name, os, version, processor, architecture, ip)

**time** [prints or returns the time]     _BetterPrinting.system.time({optional write print_val=False to use this as a variable})

**date** [prints or returns the date]     _BetterPrinting.system.date({optional write print_val=False to use this as a variable})

**tasks** [prints out the current tasks (works only in windows and Linux)]     _BetterPrinting.system.tasks()

### class ui:

**title_bar** [prints a title bar with a text]     _BetterPrinting.ui.title_bar(Title, {optional}spaces=number of spaces)

**text_box** [prints a text box with any amount of text]     _BetterPrinting.ui.text_box(text, text, text {any amount}, {optional}free_line = even number, {optional}rounded_edges= True or False)
