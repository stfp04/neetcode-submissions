class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        k = 0
        i = 0
        while i < len(arr) - 1:
            maximum = -1

            j = i + 1
            while j < len(arr):
                if arr[j] > maximum:
                    maximum = arr[j]
                    k = j
                j = j + 1

            while i < k:
                arr[i] = maximum
                i = i + 1
            
        arr[-1] = -1
        return arr
            