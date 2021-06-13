# BetterPrinting
A python library for "better" printing 

BetterPrinting is a library for easy to use printing actions!

<hr>

### Instalation

Ensure you have at least Python 3.

 ```
 pip install BetterPrinting
 or
 pip3 install BetterPrinting
 ```

If you dont have following libaries installed go and install them too.

[random, string, termcolor]

random and string are standard Python libraries

Here is 
<a href="https://pypi.org/project/termcolor/">termcolor</a>

<hr>

### Usage

 ```
import BetterPrinting as bp
 ```
 
How to use the package?

 ```Python
 import BetterPrinting as bp

bp.color("This is a green demo text!", "green")
bp.oneLine("Password Generator!")
t = input("How long should the password be? ")
bp.randmSTR(int(t))
 
 ```
 
 Result:
 
 ![image](https://user-images.githubusercontent.com/83476809/121803160-80742280-cc40-11eb-8fe4-2596d912b238.png)

<hr>

 ### Some examples
 
 Passwords:
 
 ```Python
 import BetterPrinting as bp

bp.twoLine("----This is a easy Password creator---", "Lets start!\n")

x = input('input the length of your password here: ')

bp.randmSTR(int(x)) 
 ```

Output:

![image](https://user-images.githubusercontent.com/83476809/121803530-69363480-cc42-11eb-9252-696a14bfc9d4.png)

Word splitter:

```Python
import BetterPrinting as bp

bp.oneLine("Text splitter!")

text='Lorem, ipsum, dolor, sit, amet, consectetur, adipisicing, elit, ' \
     'sed, do, eiusmod, tempor, incididunt, ut, labore, et, dolore, magna, aliqua. ' \
     'Ut, enim, ad, minim, veniam, quis, nostrud, exercitation, ullamco, laboris, nisi, ut, ' \
     'aliquip, ex.'

bp.splitWRD(text)
```

Output:

![image](https://user-images.githubusercontent.com/83476809/121803584-a8fd1c00-cc42-11eb-882c-4c433e2204f5.png)

Faster writing:

```Python
from BetterPrinting import threeLine, twoLine

threeLine("[1] Today I will go to work!", "[2] Today I will work in my garden", "[3] Today i will go hiking!")
twoLine("[4] Today I will learn Python", "[5] Today I wíll just relax")
```

Output:

![image](https://user-images.githubusercontent.com/83476809/121803736-33458000-cc43-11eb-9246-de6eb2ea2892.png)

<hr>

### Why?

This is not a professional library and it is not the best to make some new inventions!
It sould be more like a fun project for me!
I hope I could maybe help someone with it :)
