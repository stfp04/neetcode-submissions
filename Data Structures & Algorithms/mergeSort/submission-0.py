# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:

    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        end = len(pairs) - 1

        if end <= 0:
            return pairs
        
        return self.mergeAux(pairs, 0, end)

    def mergeAux(self, pairs, start, end):
        if end - start <= 0:
            print(f"\tMergeAux: returning {pairs[start:(end + 1)][0].key}")
            return pairs[start:(end + 1)]

        middle = ( (end - start) // 2 ) + start
        print(f"MergeAux for ({start} {end})")
        print(f"Calling recursions for: ({start} {middle})")
        pair1 = self.mergeAux(pairs, start, middle)
        print(f"Calling recursions for: ({middle + 1} {end})")
        pair2 = self.mergeAux(pairs, middle + 1, end)
        print(f"Merging ({start} {middle} {end})")
        return self.merge(pair1, pair2)

    def merge(self, pair1, pair2):
        arr = []
        i, j = 0, 0
        cond = True
        while cond:
            if pair1[i].key <= pair2[j].key:
                arr.append(pair1[i])
                i = i + 1
            else:
                arr.append(pair2[j])
                j = j + 1

            if i >= len(pair1):
                arr += pair2[j:]
                break
            if j >= len(pair2):
                arr += pair1[i:]
                break

        return arr