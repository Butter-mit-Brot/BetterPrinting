#### The ui class

Title bar:

```Python
import BetterPrinting as bp

bp.ui.title_bar("My wonderful Title")

```

Output:

![image](https://user-images.githubusercontent.com/83476809/144720416-a9375ad3-013e-4c31-b215-97850f7c1774.png)


Text box:

```Python
import BetterPrinting as bp

bp.ui.text_box("My Text Box", "", "This is a test Text", "this one too", "and me too", "I am a text too")

```

Output:

![image](https://user-images.githubusercontent.com/83476809/144720533-266ecc97-fb8d-441e-8c3c-19ce8306c7b9.png)


Show a list:

```Python
import BetterPrinting as bp

lst = ['List item1', 'List item2', 'List item3', 'List item4', 10000, 2.0, True, (1, "Yes"), ["Yes", "No", "maybe"]]

bp.ui.list(lst, "THE LIST OF...")

```

Output:

![image](https://user-images.githubusercontent.com/83476809/148270712-526716b1-d965-44fe-bc16-ebcfebc31876.png)


Number: 

```Python
import BetterPrinting as bp

bp.ui.number("Option1", "Option2", "Option3")

```

Output:

![image](https://user-images.githubusercontent.com/83476809/148271053-9ca8116d-92c3-409a-b0dc-b82ae8c27f2f.png)


Ascii Label:

```Python
import BetterPrinting as bp

ss = """
   __   _   
 _(  )-( )_ 
(_        _)
  (__)-(_)
"""

bp.ui.ascii_label(ss, "My wonderful text", 4, space=2)

```

Output:

![image](https://user-images.githubusercontent.com/83476809/148271283-c470ae45-24bc-4224-9299-d6d34bba0d16.png)
