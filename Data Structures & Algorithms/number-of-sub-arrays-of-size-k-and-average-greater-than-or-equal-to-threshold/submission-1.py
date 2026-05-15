class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)
        limit = threshold * k
        L = 0
        
        res = 0
        localSum = 0
        for R in range(n):
            localSum += arr[R]
            if R - L + 1 > k:
                localSum -= arr[L]
                L += 1
            if R - L + 1 == k and localSum >= limit:
                res += 1

        return res

