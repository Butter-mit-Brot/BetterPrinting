# The draw class

The draw class is used to draw into your terminal.

### How to use it:

"Import draw"

```Python
from BetterPrinting import draw
```

"store draw in a variable and choose canvas size" _optional you can choose wich letter should be used for drawing standard: #_

```Python
from BetterPrinting import draw

drawing = draw(20, 20)
```

"now you can use all the functions () and at the end write _variable name_.done() "

```Python
from BetterPrinting import draw
drawing = draw(20, 20)

drawing.forward(2)
drawing.turn("down")
drawing.forward(5)
drawing.turn("right")
drawing.forward(4)
drawing.turn("up")
drawing.forward(3)
drawing.turn("left")
drawing.forward(2)

drawing.done()
```

Output:

![image](https://user-images.githubusercontent.com/83476809/194707601-1bf219de-7fe4-4c5f-813a-6975baf4f632.png)


### function list:

#### forward:

(goes forward an specific amount of characters in set direction)

_var_name.forward(distance)_

```Python
from BetterPrinting import draw

drawing = draw(20, 20)

drawing.forward(2)
drawing.done()
```

#### turn:

(turns you into set direction [does not draw])

_var_name.turn(direction)_ 

```Python
from BetterPrinting import draw

drawing = draw(20, 20)

drawing.turn("down")
drawing.forward(4)
drawing.done()
```
