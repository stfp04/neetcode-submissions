class Solution:
    def isPalindrome(self, s: str) -> bool:
        c = [ch.lower() for ch in s if ch.isalnum()]
        L, R = 0, len(c) - 1
        while L < R:
            if c[L] != c[R]:
                return False
            L += 1
            R -= 1
        return True