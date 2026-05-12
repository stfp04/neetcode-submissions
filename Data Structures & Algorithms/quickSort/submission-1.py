# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
        
    def quickSortHelper(self, pairs: List[Pair], start, end) -> List[Pair]:
        if end - start <= 0:
            return pairs
            
        pivot = pairs[end]
        left = start
        for i in range(start, end):
            if pairs[i].key < pivot.key:
                tmp = pairs[left]
                pairs[left] = pairs[i]
                pairs[i] = tmp
                left = left + 1

        pairs[end] = pairs[left]
        pairs[left] = pivot

        self.quickSortHelper(pairs, start, left - 1)
        self.quickSortHelper(pairs, left + 1, end)

        return pairs

    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        end = len(pairs) - 1
        return self.quickSortHelper(pairs, 0, end)