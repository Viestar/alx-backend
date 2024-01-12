#!/usr/bin/env python3
""" Simple helper function that computes pages """

from typing import Tuple, List, Dict
import csv
import math


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
        pass


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Returns a size 2 tuple with a start and end indices """
    start = 0
    end = 0
    for p in range(page):
        start = end
        end = end + page_size
        return (start, end)


def get_page(self, page: int = 1, page_size: int = 10) -> List[list]:
    """ Return the correct list of rows after pagination """
    assert type(page) == int and page > 0 and type(page_size) == int \
        and page_size > 0

    data = self.dataset()
    try:
        index = index_range(page, page_size)
        return data[index[0]: index[1]]
    except IndexError:
        return []


def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[int, int, List[list], int, int, int]:
    """ Returns a dictionary with the pagination details """
    data = self.dataset()
    index = index_range(page, page_size)
    data = get_page(page, page_size)
