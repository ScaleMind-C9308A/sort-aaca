import math
import sys
from heapq import heappush, heappop
from typing import List

import os, sys
sys.path.append(os.getcwd())
from base.core import Sort

class IntroSort(Sort):
    def __init__(self, mode, backbone="insert", min_size = 16) -> None:
        super().__init__(mode, backbone)
    
    def __call__(self, _list: List):
        start_time = self._get_time()

        depthLimit = 2 * math.floor(math.log2(len(_list) - 1))
        self._introsort(_list, 0, len(_list) - 1, depthLimit)

        end_time = self._get_time()

        if self.mode == "experiment":
            return self._sub_time(start_time, end_time)
        elif self.mode == "production":
            return _list

    def _heapsort(self, _list, left: int, right: int):
        h = []
    
        for idx in range(left, right):
            heappush(h, _list[idx])
        arr = []
    
        arr = arr + [heappop(h) for i in range(len(h))]

        _list[left:right] = arr
    
    def _partition(self, _list: List, left: int, right: int):
        # print(type(_list))
        pivot = _list[right]
    
        i = left - 1
    
        for j in range(left, right):
    
            if _list[j] <= pivot:
    
                i = i + 1
                (_list[i], _list[j]) = (_list[j], _list[i])

        (_list[i + 1], _list[right]) = (_list[right], _list[i + 1])
        return i + 1

    def _get_optimal_pivot(self, _list:List, a:int, b:int, d:int):
        A = _list[a]
        B = _list[b]
        C = _list[d]
    
        if A <= B and B <= C:
            return b
        if C <= B and B <= A:
            return b
        if B <= A and A <= C:
            return a
        if C <= A and A <= B:
            return a
        if B <= C and C <= A:
            return d
        if A <= C and C <= B:
            return d
    
    def _introsort(self, _list: List, left: int, right: int, depthLimit: int):
        size = right - left
        if size < 16:    
            self.bb_map[self.bb](_list, left, right)
            return
    
        if depthLimit == 0:    
            self._heapsort()
            return
    
        pivot = self._get_optimal_pivot(_list, left, left + size // 2, right)
        _list[pivot], _list[right] = _list[right], _list[pivot]
    
        partitionPoint = self._partition(_list, left, right)
    
        self._introsort(_list, left, partitionPoint - 1, depthLimit - 1)
        self._introsort(_list, partitionPoint + 1, right, depthLimit - 1)

if __name__ == "__main__":
    intro_sort = IntroSort(mode="experiment", backbone="select", min_size=16)

    arr = [-2, 7, 15, -14, 0, 15, 0, 7, -7, -4, -13, 5, 8, -14, 12]

    print("Given Array is")
    print(arr)

    time = intro_sort(arr)

    print("After Sorting Array is")
    print(arr)

    print(f"Time : {time}")