import os, sys
sys.path.append(os.getcwd())

from typing import List
from base.core import Sort

class TimSort(Sort):
    def __init__(self, mode, backbone="insert", min_merge = 32) -> None:
        super().__init__(mode, backbone)

        self.min_merge = min_merge

    def __call__(self, _list: List):
        start_time = self._get_time()
        n = len(_list)
        minRun = self._get_min_run(n)
    
        for start in range(0, n, minRun):
            end = min(start + minRun - 1, n - 1)
            self.bb_map[self.bb](_list, start, end)
    
        size = minRun
        while size < n:
            for left in range(0, n, 2 * size):
                mid = min(n - 1, left + size - 1)
                right = min((left + 2 * size - 1), (n - 1))
                if mid < right:
                    self._merge(_list, left, mid, right)
    
            size = 2 * size
        end_time = self._get_time()

        if self.mode == "experiment":
            return self._sub_time(start_time, end_time)
        elif self.mode == "production":
            return _list

    def _get_min_run(self, size):
        r = 0
        while size >= self.min_merge:
            r |= size & 1
            size >>= 1
        return size + r
    
    def _merge(self, _list, l, m, r):
        len1, len2 = m - l + 1, r - m
        left, right = [], []
        for i in range(0, len1):
            left.append(_list[l + i])
        for i in range(0, len2):
            right.append(_list[m + 1 + i])
    
        i, j, k = 0, 0, l

        while i < len1 and j < len2:
            if left[i] <= right[j]:
                _list[k] = left[i]
                i += 1
    
            else:
                _list[k] = right[j]
                j += 1
    
            k += 1

        while i < len1:
            _list[k] = left[i]
            k += 1
            i += 1

        while j < len2:
            _list[k] = right[j]
            k += 1
            j += 1

if __name__ == "__main__":
    timsort = TimSort(mode="experiment", backbone="select", min_merge=32)

    arr = [-2, 7, 15, -14, 0, 15, 0, 7, -7, -4, -13, 5, 8, -14, 12]

    print("Given Array is")
    print(arr)

    time = timsort(arr)

    print("After Sorting Array is")
    print(arr)

    print(f"Time : {time}")