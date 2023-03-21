from config import length, height


class Pixel:
    def __init__(self, red, green, blue, x, y):
        self.red = red
        self.green = green
        self.blue = blue
        # Ensure x and y values are within screen bounds
        self.x = min(max(x, 0), length-1)
        self.y = min(max(y, 0), height-1)