class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)

    def get_diagonal(self):
        return (self.width**2 + self.height**2)**.5

    def get_picture(self):
        if self.height > 50 or self.width > 50:
            return 'Too big for picture.'
        else:
            return ((("*" * self.width) + "\n") * self.height)

    def get_amount_inside(self, fig):
        print(self.get_area())
        print(fig.get_area)
        return self.get_area() // fig.get_area()

    def __str__(self):
        return 'Rectangle(width=' + str(self.width) + ', height=' + str(
            self.height) + ')'


class Square(Rectangle):
    def __init__(self, side):
        self.height = side
        self.width = side

    def set_side(self, side):
        self.height = side
        self.width = side

    def set_width(self, side):
        self.width = side

    def set_height(self, side):
        self.height = side

    def __str__(self):
        return 'Square(side=' + str(self.width) + ')'
