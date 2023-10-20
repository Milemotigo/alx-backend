#!/usr/bin/env python3
'''a function named index_range that takes two integer arguments page and page_size
'''


def index_range(page, page_size):
    '''
    A function that that take two int and returns
    a tuple
    '''
    start = (page - 1) * page_size
    end = start + page_size

    return(start, end)