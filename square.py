# square.py

class Square:
    def __init__(self, x, y, size, canvas, color="white"):
        self.x = x
        self.y = y
        self.size = size
        self.canvas = canvas
        self.color = color
        self.rect = self.canvas.create_rectangle(
            x * size, y * size, (x + 1) * size, (y + 1) * size, outline="black"
        )

    def set_color(self, color):
        self.canvas.itemconfig(self.rect, fill=color)

    def set_outline(self, outline_color, outline_width):
        self.canvas.itemconfig(self.rect, outline=outline_color, width=outline_width)
