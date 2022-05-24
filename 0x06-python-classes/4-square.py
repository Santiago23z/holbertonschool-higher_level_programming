#!/usr/bin/python3
"""define a square class"""


class Square:
    """A simple class without methods or public attributes"""

    def __init__(self, size=0):
        """instantion safe of an  square"""
        self.__size = size

    @property
    def size(self):
        """int: return the size of thr square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """sets the atributte"""
        if type(value) == int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """int: return the area of the square"""
        return (self.__size ** 2)
