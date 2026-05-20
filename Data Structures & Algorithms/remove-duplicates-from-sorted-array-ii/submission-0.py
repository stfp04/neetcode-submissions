class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L, R, total = 0, 0, 0
        last = None

        while R < len(nums):
            cnt = 1

            while nums[R] == last:
                if cnt < 2:
                    cnt += 1
                    nums[L] = nums[R]
                    L += 1
                    total += 1
                R += 1

                if R >= len(nums):
                    return total

            nums[L] = nums[R]
            L += 1
            total += 1

            last = nums[R]
            R += 1
        
        return total
            