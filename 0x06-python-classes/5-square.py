#!/usr/bin/python3
"""define a sqaure class"""


class Square:
    """A simple class without methods or public attributes"""

    def __init__(self, size=0):
        """instantion safe of an square"""
        self.__size = size

    @property
    def size(self):
        """int: return the size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """sets the attribute size"""
        if type(value) == int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def are(self):
        """int: return the area of the square"""
        return (self.__size ** 2)

    def my_print(self):
        """prints the square with the char '#'"""
        if self.__size != 0:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print("")
        else:
            print("")
