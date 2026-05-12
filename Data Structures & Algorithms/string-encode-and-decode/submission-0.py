class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join([f"{len(s)}#{s}" for s in strs])


    def decode(self, s: str) -> List[str]:
        r = []
        i = 0
        print(s)
        while i < len(s):
            l = 0
            while s[i] != '#':
                l += int(s[i])
                l *= 10
                i += 1
            l //= 10

            i += 1

            st = ""
            while l > 0:
                st += s[i]
                l -= 1
                i+= 1
            r.append(st)
        return r
        






