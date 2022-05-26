#!/usr/bin/python3
"""
add_integer:
    check if parameters are int
    Return sum of parameters
"""



def add_integer(a, b=98):
    """Checks if int, 
    otherwise return sum
    """
    if type(a) == float or type(b) == float:
        a = int(a)
        b = int(b)
    
    if type(a) != int:
        raise TypeError("a must be an integer")
    elif type(b) != int:
        raise TypeError("b must be an integer")
    else: 
        return a + b

