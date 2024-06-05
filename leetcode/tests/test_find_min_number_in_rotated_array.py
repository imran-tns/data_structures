from typing import List
from leetcode.find_min_in_rotated_array import findMin


def test_find_min():
    assert findMin([3, 4, 5, 6, 1, 2]) == 1
    assert findMin([4, 5, 0, 1, 2, 3]) == 0
    assert findMin([4, 5, 6, 7]) == 4
    assert findMin([2, 1]) == 1
    assert findMin([3, 4, 5, 1, 2]) == 1
    assert findMin([4, 5, 6, 7, 0, 1, 2]) == 0
