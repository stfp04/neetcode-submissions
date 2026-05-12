class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = {}
        for ch in s:
            if ch in chars:
                chars[ch] += 1
            else:
                chars[ch] = 1

        for ch in t:
            if ch not in chars:
                return False
            chars[ch] -= 1
            if chars[ch] == 0:
                del chars[ch]

        if len(chars):
            return False
        return True
        