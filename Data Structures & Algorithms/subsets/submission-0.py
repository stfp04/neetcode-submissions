class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]

        subset = [[]]
        for i in range(len(nums)):
            i_value = nums[i]
            subset.append([i_value])
            currLen = len(subset)
            for j in range(1,currLen - 1):
                print(subset[j])
                print(subset[currLen - 1])
                print("Next j")
                j_value = subset[j] + subset[currLen - 1]
                subset.append(j_value)

            print(subset)
            print("Acabou\n")
        return subset                
                
                
                
