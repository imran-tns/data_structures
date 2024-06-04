from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = 0
        total_area = 0

        while left < len(height) - 1:
            if height[left]:
                right += 1
                while height[left] > height[right]:
                    right += 1
                    if right == len(height):
                        return total_area
                    if right+1 < len(height):
                        if height[right + 1] < height[right] > height[right - 1]:
                            break

                min_height = min(height[left], height[right])
                left += 1
                while left < right:
                    total_area += min_height - height[left]
                    left += 1
            else:
                left += 1
                right += 1
        return total_area
