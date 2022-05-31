#!/usr/bin/python3

'''the class is defined here
'''


class Rectangle():

    number_of_instances = 0
    print_symbol = '#'
    
    def __init__(self, width=0, height=0):
        ''' instantiation
        '''
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
    
    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise TypeError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height 

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        res = ""
        if self.__width == 0 or self.__height == 0:
            return res
        
        for i in range(self.__height):
            for i2 in range(self.__width):
                res += str(self.print_symbol)
            if i != self.__height - 1:
                res += '\n'
        return res

    def __repr__(self):
        w = str(self.__width)
        h = str(self.__height)

        res = "Rectangle(" + w + ", " + h + ")"
        return res

    def __del__(self):
        """ print a message for del
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
