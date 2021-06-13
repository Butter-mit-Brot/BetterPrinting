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

text= 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et ' \
      'dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores ' \
      'et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.'

bp.splitWRD(text)
```

Output:

![image](https://user-images.githubusercontent.com/83476809/121819941-30bd4780-cc90-11eb-9fe9-55d67e04396b.png)

Faster writing:

```Python
from BetterPrinting import threeLine, twoLine

threeLine("[1] Today I will go to work!", "[2] Today I will work in my garden", "[3] Today i will go hiking!")
twoLine("[4] Today I will learn Python", "[5] Today I wíll just relax")
```

Output:

![image](https://user-images.githubusercontent.com/83476809/121803736-33458000-cc43-11eb-9246-de6eb2ea2892.png)

Easy to use file creator:

```Python
import BetterPrinting as bp

tex= 'This is a test text!'

bp.creatF("Hello.txt", tex)

bp.oneLine("[Finished]")
```

Output:

![image](https://user-images.githubusercontent.com/83476809/121820048-dec8f180-cc90-11eb-866d-4f6aa7d95a59.png)
![image](https://user-images.githubusercontent.com/83476809/121820057-e8eaf000-cc90-11eb-9b74-346be28073ef.png)

<hr>

### Command explanation

-----------------------

**oneLine** [1 line normal print] _BetterPrinting.oneLine("text")_

**twoLine** [two lines] _BetterPrinting.twoLine("text", "text2")_

**threeLine** [three lines] _BetterPrinting.threeLine("text", "text2", "text3")_

**fourLine** [four lines] _BetterPrinting.fourLine("text", "text2", "text3", "text4")_

**fiveLine** [five lines] _BetterPrinting.fiveLine("text", "text2", "text3", "text4", "text5")_

**color** [puts out a colored version of your text] _BetterPrinting.color("text", "color for example red")_

**splitWRD** (split word)[makes a big text to an list of words] _BetterPrinting.splitWRD("Splits the text if space is between the words")_

**randmSTR** (random string)[prints out a random String of letters, numbers and special characters] _BetterPrinting.randmSTR(number)_

**randmLTR** (random letters)[prints out a random combination of letters] _BetterPrinting.randmLTR(number)_

**randmDIG** (random digits)[prints out a random combination of numbers] _BetterPrinting.randmDIG(number)_

**randmSYM** (random symbols)[prints out a random combination of special characters] _BetterPrinting.randmSYM(number)_

**creatF** (create File)[creates a file] _BetterPrinting.creatF("Filename", "text")_

<hr>

### Why?

This is not a professional library and it is not the best to make some new inventions!
It sould be more like a fun project for me!
I hope I could maybe help someone with it :)
