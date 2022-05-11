#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def repetido(n):
        return (n if n != search else replace)
    return list(map(repetido, my_list)) 