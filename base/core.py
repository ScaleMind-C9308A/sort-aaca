import os, sys
from typing import List
from datetime import datetime

class Sort:
    def __init__(self, mode, backbone = "insert") -> None:
        self.mode = mode
        self.bb = backbone
        self.bb_map = {
            "insert" : self._insertion_sort,
            "bubble" : self._bubble_sort,
            "select" : self._selection_sort
        }

    def __call__(self, _list: List):
        raise not NotImplementedError
    
    def _insertion_sort(self, _list: List, left: int, right: int):
        for i in range(left + 1, right + 1):
            j = i
            while j > left and _list[j] < _list[j - 1]:
                _list[j], _list[j - 1] = _list[j - 1], _list[j]
                j -= 1
    
    def _bubble_sort(self, _list: List, left: int, right: int):
        swapped = False
        for n in range(right, left, -1):
            for i in range(n):
                if _list[i] > _list[i + 1]:
                    swapped = True
                    _list[i], _list[i + 1] = _list[i + 1], _list[i]       
            if not swapped:
                return
    
    def _selection_sort(self, _list: List, left: int, right: int):
        for i in range(left, right):
            min_idx = i

            for j in range(i + 1, right):
                if _list[j] < _list[min_idx]:
                    min_idx = j
            _list[i], _list[min_idx] = _list[min_idx], _list[i]
    
    def _get_time(self):
        return datetime.now()
    
    def _sub_time(self, start: datetime, stop: datetime):
        return (stop - start).microseconds
    
    def get_mode(self):
        return self.mode
    
    def set_mode(self, mode):
        self.mode = mode
    