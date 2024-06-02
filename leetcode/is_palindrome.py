class Solution:
    def is_palindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1

        while right >= left:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            if s[left] != s[right]:
                return False
            else:
                left += 1
                right -= 1
        return True
