#!/usr/bin/env python3
"""
Write a function named index_range that takes two
integer arguments page and page_size.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """
    page : int
    page_size : int
    return : tuple
    """
    begin = (page - 1) * page_size
    return (begin, begin + page_size)
