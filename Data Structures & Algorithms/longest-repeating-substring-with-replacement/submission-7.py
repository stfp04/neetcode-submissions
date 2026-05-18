class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L, length = 0, 0
        maxChar, maxCount = 0, 0
        toReplace = 0
        letters = {}

        for R in range(len(s)):
            if s[R] not in letters:
                letters[s[R]] = 0
            letters[s[R]] += 1


            if letters[s[R]] > maxCount:
                maxChar = s[R]
                maxCount = letters[s[R]]
                
            while (R - L + 1) - maxCount > k:
                letters[s[L]] -= 1
                
                if s[L] == maxChar:
                    maxChar, maxCount = max(letters.items(), key=lambda x: x[1])

                if letters[s[L]] == 0:
                    del letters[s[L]]

                L += 1


            length = max(length, R - L + 1)

        return length