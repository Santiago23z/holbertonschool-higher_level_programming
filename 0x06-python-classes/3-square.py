#!/usr/bin/python3
"""define a square class"""


class Square:
    """a simple class"""

    def __init__(self, size=0):
        """inicializaion safe of an square"""
        if type(size) == int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """int: return the area of rhe squuare"""
        return (self.__size ** 2)

    
