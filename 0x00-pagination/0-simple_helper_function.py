#!/usr/bin/env python3
'''a function named index_range that takes two integer arguments page and page_size
'''


def index_range(page: int, page_size: int) -> tuple:
    '''
    A function that that take two int and returns
    a tuple
    '''
    start = (page - 1) * page_size
    end = start + page_size

    return(start, end)

print(index_range(1, 10))
