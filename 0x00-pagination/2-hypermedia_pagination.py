#!/usr/bin/env python3
"""
Write a function named index_range that takes two
integer arguments page and page_size.
"""
import csv
import math
from typing import Tuple, List, Dict


def index_range(page: int, page_size: int) -> Tuple:
    """
    page : int
    page_size : int
    return : tuple
    """
    begin = (page - 1) * page_size
    return (begin, begin + page_size)


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
        """
        page : int
        page_size : int
        return : tuple
        """
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0
        start, end = index_range(page, page_size)
        data = self.dataset()
        size = len(data)
        if start >= size:
            return []

        end = size if end > size else end
        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        page : int
        page_size : int
        return : tuple
        """
        data = get_page(page, page_size)
        size = len(data)
        total_pages = math.ceil(size / page_size)

        return {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }
