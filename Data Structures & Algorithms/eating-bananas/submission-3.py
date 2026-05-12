class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            m = (l + r) // 2
            tot = 0
            for p in piles:
                tot += math.ceil(float(p) / m)
            if tot <= h:
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1
        return res