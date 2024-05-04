import math
from typing import List


class KokoEatingBananas:
    def countHours(self, piles: List[int], bananas: int) -> int:
        hours = 0
        for i in range(len(piles)):
            hours += math.ceil(piles[i] / bananas)
        return hours
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == h:
            return max(piles)
        low, high = 1, max(piles)
        while low <= high:
            # mid = number of bananas can be eaten in a day
            mid = (low + high) // 2
            hours = self.countHours(piles, mid)
            # if hours are more we need to eat more
            if hours > h:
                low = mid + 1
            # if hours are less we need to eat less to take more time
            else:
                high = mid - 1
        return low
