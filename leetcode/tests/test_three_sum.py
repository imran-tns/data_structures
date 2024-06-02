def test_three_sum_from_leetcode():
    from leetcode.three_sum import Solution
    assert Solution().threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]

    assert Solution().threeSum([]) == []

    assert Solution().threeSum([0, 0, 0]) == [[0, 0, 0]]
