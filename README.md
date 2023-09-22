# BetterPrinting
A python library for "better" printing 

BetterPrinting is a library for easy to use printing actions and functions arround printing!

<hr>

Pypi: https://pypi.org/project/BetterPrinting/

Version: 0.7.4

<hr>

### Installation

Ensure you have at least Python 3.

 ```
 pip install -U BetterPrinting
 or
 pip3 install -U BetterPrinting
 ```
 
<hr>

### Class explanations

<a href='https://github.com/Butter-mit-Brot/BetterPrinting/blob/main/docs/draw.md'>The draw class</a>

<a href='https://github.com/Butter-mit-Brot/BetterPrinting/blob/main/docs/ui.md#the-ui-class'>The ui class</a>

<a href='https://github.com/Butter-mit-Brot/BetterPrinting/blob/main/docs/system.md#the-system-class'>The system class</a>

<hr>

### Command explanation

<a href="https://github.com/Butter-mit-Brot/BetterPrinting/blob/main/Commands.md">All commands here</a>

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

Text box:

```Python
import BetterPrinting as bp

bp.ui.text_box("My new game!", "press Enter to start", rounded_edges=True)
```

Output:

![image](https://user-images.githubusercontent.com/83476809/194708511-68a8bb8c-813b-40de-b212-795e59f0ebb2.png)

Multi line:

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
