class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        for i in range(0,n+1):
            c = i
            r = 0
            while c > 0:
                r += 1 if c&1==1 else 0
                c >>= 1
            output.append(r)
        return output