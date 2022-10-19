# The draw class

The draw class is used to draw into your terminal.

### How to use it:
_________________

"Import draw"

```Python
from BetterPrinting import draw
```

"store draw in a variable and choose canvas size" _optional you can choose wich letter should be used for drawing standard: #_

```Python
from BetterPrinting import draw

drawing = draw(20, 20)
```

"now you can use all the <a href="https://github.com/Butter-mit-Brot/BetterPrinting/blob/main/docs/draw.md#function-list">functions</a> and at the end write _variable name_.done() "

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


### Function list:
______________________________
#### set_pos:

(sets position on canvas)

_var_name.set_pos(x, y)_

```Python
from BetterPrinting import draw

drawing = draw(20, 20)

drawing.set_pos(0, 3)
drawing.forward(4)
drawing.done()
```

#### forward:

(goes forward an specific amount of characters in set direction)

_var_name.forward(distance)_

```Python
from BetterPrinting import draw

drawing = draw(20, 20)

drawing.forward(2)
drawing.done()
```

#### place_character:

(places 1 character)

_var_name.place_character(x, y, character)_

```Python
from BetterPrinting import draw

drawing = draw(20, 20)

drawing.place_character(3, 3, "H")
drawing.place_character(4, 3, "I")
drawing.done()
```

#### place_text:

(places text on the canvas)

_var_name.place_character(x, y, text)_

```Python
from BetterPrinting import draw

drawing = draw(20, 20)

drawing.place_text(3, 3, "Hello")
drawing.done()
```

#### turn:

(turns you into set direction [does not draw])

_var_name.turn(direction)_      
(You can only use "right", "left", "down", "up" as directions)
```Python
from BetterPrinting import draw

drawing = draw(20, 20)

drawing.turn("down")
drawing.forward(4)
drawing.done()
```

#### turn_reset:

(resets direction to right)

_var_name.turn_reset()_

```Python
from BetterPrinting import draw

drawing = draw(20, 20)

drawing.turn("down")
drawing.forward(4)
drawing.drawing.turn_reset()
drawing.forward(2)
drawing.done()
```

#### clear:

(clears canvas [does not print again])

_var_name.clear()_

```Python
from BetterPrinting import draw

drawing = draw(20, 20)

drawing.turn("down")
drawing.forward(4)
drawing.drawing.clear()
drawing.forward(2)
drawing.done()
```

#### done:

(draws the canvas)

_var_name.done()_

```Python
from BetterPrinting import draw

drawing = draw(20, 20)

drawing.forward(4)
drawing.done()
```
