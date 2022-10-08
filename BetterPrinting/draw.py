class draw:

    def __init__(self, canvas_x: int, canvas_y: int, letter: str = "#"):
        self.letter = letter
        self.canvas_x = canvas_x
        self.canvas_y = canvas_y
        self.x = 0
        self.y = 0

        self.canvas = """"""

        for x in range(self.canvas_y):
            for y in range(self.canvas_x):
                self.canvas += " "
            self.canvas += "\n"

        self.turn_direction = "right"

    def done(self):
        if self.x > self.canvas_x or self.y >= self.canvas_y:
            raise ValueError("Canvas is smaller than point you want to go or you are moving out of the canvas!")
        if self.x < 0 or self.y < 0:
            raise ValueError("Your point is smaller than the canvas or you are moving out of the canvas!")

        print(self.canvas, end="")
        # print(self.canvas.replace(" ", "#"), end="")

    def set_pos(self, x: int, y: int):
        self.x = x
        self.y = y
        self.__canvas_line(self.y, self.x, " ")

    def __canvas_line(self, line, line_pos, new_char):
        down = 0
        split_canv = self.canvas.split("\n")
        for li in range(len(split_canv)):
            if li == line:
                for char in range(len(split_canv[li])):
                    if char == line_pos:
                        x = list(split_canv[li])
                        x[char] = new_char
                        split_canv[li] = "".join(x)
        self.canvas = """"""
        for l in split_canv:
            if down == self.canvas_y:
                break
            down += 1
            self.canvas += f"{l}\n"

    def forward(self, distance: int):
        if self.turn_direction == "right":
            for dis in range(distance):
                self.__canvas_line(self.y, self.x, self.letter)
                self.x += 1

        if self.turn_direction == "left":
            for dis in range(distance):
                self.__canvas_line(self.y, self.x, self.letter)
                if (self.x - 1) < 0:
                    self.x = 0
                else:
                    self.x -= 1

        if self.turn_direction == "down":
            for dis in range(distance):
                self.__canvas_line(self.y, self.x, self.letter)
                self.y += 1

        if self.turn_direction == "up":
            for dis in range(distance):
                self.__canvas_line(self.y, self.x, self.letter)
                if (self.y - 1) < 0:
                    self.y = 0
                else:
                    self.y -= 1

    def turn(self, direction: str):
        directions = ["right", "left", "down", "up"]
        if direction not in directions:
            raise ValueError(f"You can only use {directions} as directions!")

        if direction == directions[0]:
            self.turn_direction = directions[0]
        if direction == directions[1]:
            self.turn_direction = directions[1]
        if direction == directions[2]:
            self.turn_direction = directions[2]
        if direction == directions[3]:
            self.turn_direction = directions[3]

    def turn_reset(self):
        self.turn_direction = "right"
