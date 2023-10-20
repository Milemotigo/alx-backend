#!/usr/bin/env python3
''' Hypermedia pagination'''
from typing import List

Server = __import__('1-simple_pagination').Server

def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
    