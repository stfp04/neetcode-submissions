class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        self.names = {}
        self.par = {}

        n = 0
        for account in accounts:
            name = account[0]
            self.names[n] = name

            for i in range(1, len(account)):
                email = account[i]
                if email in self.par:
                    p  = self.par[email]
                    while p != self.par.get(p, p):
                        p = self.par[p]
                    
                    if n not in self.par:
                        self.par[n] = p
                    else:
                        self.par[p] = self.par[n]
                    continue
                self.par[email] = n
            
            n += 1

        tmp = {}
        for e, p in self.par.items():
            if isinstance(e, int):
                continue

            pe = p
            while pe != self.par.get(pe, pe):
                pe = self.par[pe]

            if pe not in tmp:
                tmp[pe] = []
            tmp[pe].append(e)

        res = []
        for n, l in tmp.items():
            name = self.names[n]
            l.sort()
            res += [[name] + l]
        
        return res

                



        