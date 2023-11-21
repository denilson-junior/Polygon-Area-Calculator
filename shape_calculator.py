class Rectangle:

  def __init__(self, width, height) -> None:
    self.width = width
    self.height = height

  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return 2 * self.width + 2 * self.height

  def get_diagonal(self):
    return (self.width**2 + self.height**2)**.5

  def get_picture(self):
    if self.height > 50 or self.width > 50:
      return "Too big for picture."

    draw = ""

    for line in range(self.height):
      draw += "*" * self.width
      draw += "\n"

    return draw

  def get_amount_inside(self, shape):
    height_calc = int(self.height / shape.height)
    width_calc = int(self.width / shape.width)

    return height_calc * width_calc

class Square(Rectangle):

  def __init__(self, side) -> None:
    self.width = side
    self.height = side

  def __str__(self):
    return "Square(side=" + str(self.width) + ")"

  def set_side(self, side):
    self.width = side
    self.height = side
