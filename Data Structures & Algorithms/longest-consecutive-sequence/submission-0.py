class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        par = {}

        for num in nums:
            if num in par:
                continue

            p = par.get(num - 1, num)
            while p != par.get(p - 1, p):
                par[p] = par.get(p - 1, p)
                p = par[p]
            par[num] = p

        child = {}
        res = 0
        for p, c in par.items():
            pp = par.get(p - 1, p)
            while pp != par.get(pp - 1, pp):
                par[pp] = par[pp - 1]
                pp = par[pp]
            child[pp] = child.get(pp, 0) + 1
            
            res = max(child[pp], res)

        return res