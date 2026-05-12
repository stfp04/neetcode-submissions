
class Solution:
    def climbStairs(self, n: int) -> int:
        w1,w2=1,0

        for i in range(n):
           temp = w1 + w2
           w2=w1
           w1=temp
        return w1