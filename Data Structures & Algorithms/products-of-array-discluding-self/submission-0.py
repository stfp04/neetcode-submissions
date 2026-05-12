class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros, mul = 0, 1
        for num in nums:
            if num:
                mul *= num
            else:
                zeros += 1

        results = []
        for num in nums:
            if zeros == 1:
                if num:
                    results.append(0)
                else:
                    results.append(mul)
            elif zeros > 1:
                results.append(0)
            else:
                if not num:
                    results.append(mul)
                    continue
                results.append(mul//num)

        return results