class UnionFind:
    
    def __init__(self, n: int):
        self.par = {}
        self.rank = {}

        for i in range(0, n):
            self.par[i] = i
            self.rank[i] = 0

    def find(self, x: int) -> int:
        p = self.par[x]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p

    def isSameComponent(self, x: int, y: int) -> bool:
        p1, p2 = self.find(x), self.find(y)
        return p1 == p2

    def union(self, x: int, y: int) -> bool:
        p1, p2 = self.find(x), self.find(y)
        if p1 == p2:
            return False

        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p2] > self.rank[p1]:
            self.par[p1] = p2
        else:
            self.par[p1] = p2
            self.rank[p2] += 1

        return True

    def getNumComponents(self) -> int:
        parents = set({})
        res = 0
        for i in range(len(self.par)):
            par = self.find(i)
            if par in parents:
                continue
            parents.add(par)
            res += 1
        return res

