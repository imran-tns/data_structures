from leetcode.trapping_rain_water import Solution


# unit test for trapping rain water leetcode problem
def test_trapping_rain_water():
    assert Solution().trap([0, 2, 0, 3, 1, 0, 1, 3, 2, 1]) == 9
    assert Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6

