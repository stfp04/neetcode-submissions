class Solution:
    def hoursEatingBananas(self, piles, rate):
        hours = 0
        for pile in piles:
            hours += pile // rate
            rest = pile % rate
            if rest > 0:
                hours += 1
        return hours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minRate, maxRate = 1, max(piles)

        while minRate < maxRate:
            midRate = (minRate + maxRate) // 2
            eatingHours = self.hoursEatingBananas(piles, midRate)

            if eatingHours > h:
                minRate = midRate + 1
            elif eatingHours <= h:
                maxRate = midRate

        return minRate




