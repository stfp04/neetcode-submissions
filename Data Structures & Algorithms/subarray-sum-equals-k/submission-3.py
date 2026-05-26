class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res=curSum=0
        prefixsum={0:1}
        for num in nums:
            curSum+=num
            diff=curSum-k
            res+=prefixsum.get(diff,0)
            prefixsum[curSum]=1+prefixsum.get(curSum,0)
        return res
       
        
