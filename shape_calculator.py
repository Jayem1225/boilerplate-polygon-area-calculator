class Rectangle:
    height = 0
    width = 0
    
    def __init__(self, height=0, width=0):
        self.set_height(height)
        self.set_width(width)
        
    def set_width(self, width):
        self.width = width
        
    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.height * self.width
    
    def get_perimeter(self):
        return 2*self.width + 2*self.height
    
    def get_diagonal(self):
        return (width ** 2 + height ** 2) ** .5
    
    def get_picture(self):
        poly_str = ""
        for i in range(0, self.height):
            poly_str += f"\n{'*'*self.width}"
        return poly_str


class Square(Rectangle):
    def __init__(self, side):
        super(Square, self).__init__(side,side)
        
    def set_side(self, side):
        self.set_height = side
        self.set_width = side
