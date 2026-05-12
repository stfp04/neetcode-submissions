class MinHeap:
    
    def __init__(self):
        self.heap = []

    def push(self, val: int) -> None:
        self.heap.append(val)
        i = len(self.heap) - 1
        while i > 0:
            if self.heap[i] >= self.heap[(i - 1) // 2]:
                return
 
            tmp = self.heap[(i - 1) // 2]
            self.heap[(i - 1) // 2] = self.heap[i]
            self.heap[i] = tmp
            i = (i - 1) // 2

    def pop(self) -> int:
        n = len(self.heap)

        if n == 0:
            return -1
        elif n == 1:
            return self.heap.pop()

        val = self.heap[0]
        self.heap[0] = self.heap[n - 1]
        self.heap.pop()

        i = 0
        while i * 2 + 1 < len(self.heap):
            if i * 2 + 2 < len(self.heap) and \
            self.heap[i * 2 + 2] < self.heap[i * 2 + 1] and \
            self.heap[i * 2 + 2] < self.heap[i]:
                tmp = self.heap[i]
                self.heap[i] = self.heap[i * 2 + 2]
                self.heap[i * 2 + 2] = tmp
                i = i * 2 + 2
            elif self.heap[i * 2 + 1] < self.heap[i]:
                tmp = self.heap[i]
                self.heap[i] = self.heap[i * 2 + 1]
                self.heap[i * 2 + 1] = tmp
                i = i * 2 + 1
            else:
                break
        return val

    def top(self) -> int:
        if not len(self.heap):
            return -1
        return self.heap[0]

    def heapify(self, nums: List[int]) -> None:
        self.heap = nums.copy()
        n = len(self.heap) - 1
        cur = (n-1) // 2
        while cur >= 0:
            i = cur
            while i * 2 + 1 < len(self.heap):
                if i * 2 + 2 < len(self.heap) and \
                self.heap[i * 2 + 2] < self.heap[i * 2 + 1] and \
                self.heap[i * 2 + 2] < self.heap[i]:
                    tmp = self.heap[i]
                    self.heap[i] = self.heap[i * 2 + 2]
                    self.heap[i * 2 + 2] = tmp
                    i = i * 2 + 2
                elif self.heap[i * 2 + 1] < self.heap[i]:
                    tmp = self.heap[i]
                    self.heap[i] = self.heap[i * 2 + 1]
                    self.heap[i * 2 + 1] = tmp
                    i = i * 2 + 1
                else:
                    break
            cur -= 1
        print(self.heap)

    