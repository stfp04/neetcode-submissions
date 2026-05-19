class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) < 2:
            return 1

        L, length = 0, 1
        sign = arr[0] > arr[1]

        for R in range(1, len(arr)):
            if arr[R] == arr[R - 1]:
                L = R
                if R < len(arr) - 1:
                    sign = arr[R + 1] > arr[R]
                    continue
                break

            cmp = arr[R] > arr[R - 1]
            if cmp != sign:
                sign = cmp
                L = R - 1
            sign = not sign
            length = max(length, R - L + 1)

        return length
