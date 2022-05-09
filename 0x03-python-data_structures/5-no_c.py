#!/usr/bin/env python3
def no_c(my_string):
    new_str = ''.join(a for a in my_string if a != "c" and a != "C")
    return(new_str)
