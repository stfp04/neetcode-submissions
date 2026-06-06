class SegmentNode:
    
    def __init__(self, total, L, R):
        self.total = total
        self.L, self.R = L, R
        self.left = self.right = None

    @staticmethod
    def build(nums: List[int], L: int, R: int) -> SegmentNode:
        if L == R:
            return SegmentNode(nums[L], L, R)

        M = (R + L) // 2
        root = SegmentNode(0, L, R)
        root.left = SegmentNode.build(nums, L, M)
        root.right = SegmentNode.build(nums, M+1, R)
        root.total = root.left.total + root.right.total
        return root

    def update(self, index: int, val: int) -> None:
        if self.L == self.R and self.L == index:
            self.total = val
            return

        M = (self.R + self.L) // 2
        if index <= M:
            self.left.update(index, val)
        elif index > M:
            self.right.update(index, val)
        self.total = self.left.total + self.right.total
        return

    def query(self, L: int, R: int) -> int:
        if self.L == L and self.R == R:
            return self.total
        
        M = (self.R + self.L) // 2
        if L > M:
            return self.right.query(L, R)
        elif R <= M:
            return self.left.query(L, R)
        else:
            return self.left.query(L, M) + self.right.query(M+1, R)
        

class SegmentTree:
    
    def __init__(self, nums: List[int]):
        self.root = SegmentNode.build(nums, 0, len(nums) - 1)
    
    def update(self, index: int, val: int) -> None:
        self.root.update(index, val)
    
    def query(self, L: int, R: int) -> int:
        return self.root.query(L, R)
