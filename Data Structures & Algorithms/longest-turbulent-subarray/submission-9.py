class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) < 2:
            return 1

        start = 1
        while start < len(arr) and arr[start - 1] == arr[start]:
            start += 1
        if start >= len(arr):
            return 1
        sign = not (arr[start - 1] > arr[start])

        L, length = start - 1, 0
        last = arr[0]
        
        for R in range(start, len(arr)):
            print(L,R)
            cmp = arr[R] > arr[R - 1]
            if arr[R] == arr[R - 1]:
                L = R
            elif cmp != sign:
                sign = cmp
                L = R - 1
            sign = not sign
            length = max(length, R - L + 1)

        return length
