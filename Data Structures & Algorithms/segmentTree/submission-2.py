class SegmentTree:
    def __init__(self, nums: List[int]):
        n = len(nums)
        self.tree = [0] * (4 * n)
        self._build(0, 0, n - 1, nums)

    def _build(self, idx: int, L: int, R: int, nums: List[int]) -> None:
        if L == R:
            self.tree[idx] = nums[L]
            return
        M = (L + R) // 2
        left = 2 * idx + 1
        right = 2 * idx + 2
        self._build(left, L, M, nums)
        self._build(right, M + 1, R, nums)
        self.tree[idx] = self.tree[left] + self.tree[right]

    def update(self, index: int, val: int) -> None:
        self._update(0, 0, len(self.tree)//4 - 1, index, val)

    def _update(self, idx: int, L: int, R: int, target: int, val: int) -> None:
        if L == R:
            self.tree[idx] = val
            return
        M = (L + R) // 2
        left = 2 * idx + 1
        right = 2 * idx + 2
        if target <= M:
            self._update(left, L, M, target, val)
        else:
            self._update(right, M + 1, R, target, val)
        self.tree[idx] = self.tree[left] + self.tree[right]

    def query(self, L: int, R: int) -> int:
        return self._query(0, 0, len(self.tree)//4 - 1, L, R)

    def _query(self, idx: int, nodeL: int, nodeR: int, qL: int, qR: int) -> int:
        # No overlap
        if qR < nodeL or qL > nodeR:
            return 0
        # Full overlap
        if qL <= nodeL and nodeR <= qR:
            return self.tree[idx]
        # Partial overlap
        M = (nodeL + nodeR) // 2
        left = 2 * idx + 1
        right = 2 * idx + 2
        return self._query(left, nodeL, M, qL, qR) + self._query(right, M + 1, nodeR, qL, qR)