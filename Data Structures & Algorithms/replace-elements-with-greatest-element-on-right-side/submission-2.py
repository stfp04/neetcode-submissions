class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        rightMax = arr[-1]
        for i in range(n - 2, -1, -1):
            tmp = arr[i]
            arr[i] = rightMax
            rightMax = max(rightMax, tmp)
        arr[-1] = -1
        return arr