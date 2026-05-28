class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.par = {}
        self.rank = {}

        edge = []
        for ai, bi in edges:
            p1, p2 = self.par.get(ai, ai), self.par.get(bi, bi)

            while p1 != self.par.get(p1, p1):
                p1 = self.par.get(p1,p1)
            while p2 != self.par.get(p2, p2):
                p2 = self.par.get(p2,p2)


            r1, r2 = self.rank.get(p1, 0), self.rank.get(p2, 0)

            if p1 == p2:
                edge = [ai, bi]
                continue

            if r1 > r2:
                self.par[p2] = p1
            elif r2 > r1:
                self.par[p1] = p2
            else:
                self.par[p1] = p2
                self.rank[p2] = r2 + 1 
        print(self.par)
        print(self.rank)
        return edge