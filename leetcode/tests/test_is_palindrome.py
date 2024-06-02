def test_is_palindrome():
    from leetcode.is_palindrome import Solution
    assert Solution().is_palindrome("A man, a plan, a canal: Panama") == True
    assert Solution().is_palindrome("race a car") == False
