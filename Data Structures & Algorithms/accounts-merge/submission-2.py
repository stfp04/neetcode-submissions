class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        self.names = {}
        self.par = {}

        n = 0
        for account in accounts:
            name = account[0]
            self.names[n] = name
            tmp = n

            n += 1
            for i in range(1, len(account)):
                email = account[i]
                p = self.par.get(email, -1)
                if p == -1:
                    self.par[email] = tmp
                else:
                    if n - 1 == tmp:
                        print("yep")
                        self.par[email] = p
                        tmp = p
                        for i in range(1, i):
                            self.par[account[i]] = p
                    else:
                        print("yo")
                        for e in self.par:
                            if e == p:
                                self.par[e] = tmp
                            if self.par[e] == p:
                                self.par[e] = tmp

        tmp = {}
        for e, p in self.par.items():
            if p not in tmp:
                tmp[p] = []
            tmp[p].append(e)
        
        res = []
        for p, l in tmp.items():
            l.sort()
            nl = [self.names[p]] + l
            res.append(nl)

        return res



        