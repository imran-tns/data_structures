from typing import List
from leetcode.find_target_in_rotated_sorted_array import Solution


def test_find_target_in_rotated_sorted_array():
    assert Solution().search([3, 4, 5, 6, 1, 2], 1) == 4
    assert Solution().search([3, 5, 6, 0, 1, 2], 4) == -1
    assert Solution().search([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert Solution().search([3, 1], 3) == 0
