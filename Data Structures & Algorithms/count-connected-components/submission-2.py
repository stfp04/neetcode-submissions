class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        npar = n
        par = {}
        for a,b in edges:
            pa = par.get(a, a)
            while pa != par.get(pa, pa):
                pa = par.get(pa, pa)


            pb = par.get(b,b)
            while pb != par.get(pb, pb):
                pb = par.get(pb, pb)

            if pa == pb:
                continue
            npar -= 1

            par[pb] = pa

        return npar