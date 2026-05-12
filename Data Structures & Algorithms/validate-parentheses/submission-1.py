class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {
            "[": "]",
            "(": ")",
            "{": "}",
        }
        for i in range(len(s)):
            ch = s[i]
            if ch in brackets:
                stack.append(ch)
            else:
                if len(stack) < 1:
                    return False
                if brackets[stack[-1]] != ch:
                    return False
                stack.pop()
        return len(stack) == 0