# BetterPrinting
A python library for "better" printing 

BetterPrinting is a library for easy to use printing actions and functions arround printing!

<hr>

### Installation

Ensure you have at least Python 3.

 ```
 pip install BetterPrinting
 or
 pip3 install BetterPrinting
 ```
 
<hr>

### Explanations

<a href='https://github.com/Butter-mit-Brot/BetterPrinting#class-explanations'>Class explanations</a>

<a href='https://github.com/Butter-mit-Brot/BetterPrinting#command-explanation'>Command explanations</a>

<hr>

### Usage

 ```
import BetterPrinting as bp
 ```
 
How to use the package?

 ```Python
import BetterPrinting as bp

bp.color("This is a green demo text!", "green")
bp.multi_lines("Password Generator!", '\n')
t = input("How long should the password be? ")
bp.random_str(int(t))
 
 ```
 
 Result:
 
![image](https://user-images.githubusercontent.com/83476809/122221733-dbf91700-ceb1-11eb-87ba-9310ece111e1.png)

<hr>

 ### Some examples
 
 Passwords:
 
 ```Python
 import BetterPrinting as bp

bp.multi_lines("----This is a easy Password creator---", "Lets start!\n")

x = input('input the length of your password here: ')

bp.random_str(int(x)) 
 ```

Output:

![image](https://user-images.githubusercontent.com/83476809/121803530-69363480-cc42-11eb-9252-696a14bfc9d4.png)

Word splitter:

```Python
import BetterPrinting as bp

bp.multi_lines("Text splitter!")

text= 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et ' \
      'dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores ' \
      'et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.'

bp.split_wrd(text)
```

Output:

![image](https://user-images.githubusercontent.com/83476809/121819941-30bd4780-cc90-11eb-9fe9-55d67e04396b.png)

Faster writing:

```Python
from BetterPrinting import multi_lines

multi_lines("[1] Today I will go to work!", "[2] Today I will work in my garden",
"[3] Today i will go hiking!", "[4] Today I will learn Python", "[5] Today I wíll just relax")
```

Output:

![image](https://user-images.githubusercontent.com/83476809/122222011-22e70c80-ceb2-11eb-94a2-89449fcb1dea.png)

A time table:

```Python
import BetterPrinting as bp

bp.break_line()
bp.multi_lines("This is a Time table", f"Time: {bp.system.time(print_val=False)}", f"Date: {bp.system.date(print_val=False)}")
bp.break_line()
```

Output:

![image](https://user-images.githubusercontent.com/83476809/142874565-ee0cc0a8-f3f7-4d43-b6eb-368f80ebc14c.png)

Print System info:

```Python
import BetterPrinting as bp

bp.break_line()
bp.system.sys_info(os=True, version=True, ip=True)
```

In Windows:

![image](https://user-images.githubusercontent.com/83476809/142875907-cb98ec6a-2caa-4796-91af-e5c81a23f4ac.png)

In Linux subsystem:

![image](https://user-images.githubusercontent.com/83476809/142876040-ca3a1666-3910-4db9-8131-c478fbcb531d.png)

<hr>

### Class explanations

<a href='https://github.com/Butter-mit-Brot/BetterPrinting/blob/main/docs/ui.md#the-ui-class'>The ui class</a>

<a href='https://github.com/Butter-mit-Brot/BetterPrinting/blob/main/docs/system.md#the-system-class'>The system class</a>

<hr>

### Command explanation

<a href="https://github.com/Butter-mit-Brot/BetterPrinting/blob/main/Commands.md">All commands here</a>

<hr>
