class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        comps = {')': '(', '}': '{', ']': '['}
        for ch in s:
            if ch == '(' or ch == '{' or ch == '[':
                stack.append(ch)
            if ch == ')' or ch == '}' or ch == ']':
                if stack:
                    if not stack.pop() == comps[ch]:
                        return False
                else:
                    return False

        return True if not stack else False