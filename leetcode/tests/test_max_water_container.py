from leetcode.max_water_container import Solution


# unit test for max water container leetcode problem
def test_max_water_container():
    assert Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert Solution().maxArea([1, 1]) == 1
    assert Solution().maxArea([4, 3, 2, 1, 4]) == 16
    assert Solution().maxArea([1, 2, 1]) == 2
    assert Solution().maxArea([1, 7, 2, 5, 4, 7, 3, 6]) == 36
    assert Solution().maxArea([2, 2, 2]) == 4
