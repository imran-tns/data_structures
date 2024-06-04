import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h == len(piles):
            return max(piles)
        piles.sort()
        k_list = range(1, piles[len(piles) - 1] + 1)

        low = 0
        high = len(k_list) - 1
        min_k = 1
        while high >= low:
            mid = int((low + high) / 2)
            k = k_list[mid]
            hours_needed = 0
            for item in piles:
                hours_needed += math.ceil(item / k)
            if hours_needed > h:
                low = mid + 1
            if hours_needed <= h:
                min_k = k
                high = mid - 1
        return min_k
