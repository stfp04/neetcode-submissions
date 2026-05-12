class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:
            return []

        queue = collections.deque()

        n = len(nums)
        res = []
        for i in range(n):
            iNum = nums[i]
            queue.append( ([iNum], iNum, i) )
            while queue:
                subset, combSum, idx = queue.popleft()
                if combSum > target:
                    continue
                elif combSum == target:
                    res.append( subset )
                    continue
                for j in range(idx, n):
                    jNum = nums[j]
                    interSum = combSum + jNum
                    queue.append( (subset + [jNum], interSum, j) )
            print(res)
        return res