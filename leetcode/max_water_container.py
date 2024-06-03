from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        largest = 0
        while right > left:
            min_height = min(heights[left], heights[right])
            width = right - left
            if heights[right] > heights[left]:
                left += 1
            else:
                right -= 1

            largest = max((min_height * width), largest)
        return largest
