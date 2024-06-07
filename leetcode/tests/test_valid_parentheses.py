from typing import List
from leetcode.valid_parentheses import Solution


def test_valid_parentheses():
    assert Solution().isValid('[]') is True
    assert Solution().isValid('([{}])') is True
    assert Solution().isValid('[(])') is False
