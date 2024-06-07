class Solution:
    def isValid(self, s: str) -> bool:
        s_stack = []
        closing_found = False

        for i in s:
            if i in ['(', '{', '[']:
                s_stack.append(i)
                closing_found = False
            elif i in [')', '}', ']']:
                if not s_stack:
                    return False
                pair = s_stack.pop() + i
                if pair not in ['()', '{}', '[]']:
                    return False
                closing_found = True
        return True and closing_found and not s_stack