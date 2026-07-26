class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'(':")",'{':'}','[':']'}
        stack = []
        for c in s:
            if c in brackets:
                stack.append(brackets[c])
            elif stack:
                if c != stack[-1]:
                    return False
                else:
                    stack.pop()
            else:
                return False
        return True if not stack else False