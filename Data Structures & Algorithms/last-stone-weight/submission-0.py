class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0

        heapq.heapify_max(stones)
        while len(stones) > 1:
            y = heapq.heappop_max(stones)
            x = heapq.heappop_max(stones) 
            
            if y == x:
                continue
            heapq.heappush_max(stones, y - x)
        
        if not len(stones):
            return 0
        return stones[0]