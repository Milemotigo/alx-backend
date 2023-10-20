#!/usr/bin/env python3
''' Hypermedia pagination'''
import csv
import math
from typing import List


index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)
        if start >= len(self.dataset()) or end < 0:
            return []
        else:
            return self.dataset()[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        return {
            "page_size": len(self.dataset()),
            "page": page,
            "data": self.dataset()[page_size:page],
            "next_page": self.dataset()[page],
            "prev_page": self.dataset(),
            "total_pages": self.dataset()
        }