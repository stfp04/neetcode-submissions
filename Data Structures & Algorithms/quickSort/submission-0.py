# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def printPairList(self, pairs):
        print("[", end="")
        for e in pairs:
            print(e.key, end=",")
        print("]")
        
    def quickSortHelper(self, pairs: List[Pair], start, end) -> List[Pair]:
        print(f"Start {start} End {end}")
        print("Before")
        self.printPairList(pairs)

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
        
        print("After")
        self.printPairList(pairs)

        self.quickSortHelper(pairs, start, left - 1)
        self.quickSortHelper(pairs, left + 1, end)

        return pairs

    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        end = len(pairs) - 1
        return self.quickSortHelper(pairs, 0, end)