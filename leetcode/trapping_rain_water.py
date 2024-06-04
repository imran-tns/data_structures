from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = 0
        total_area = 0
        max_left = []
        max_right = []
        for i in range(len(height)):
            if height[i] > left:
                left = height[i]
            max_left.append(left)
            if height[len(height) - 1 - i] > right:
                right = height[len(height) - 1 - i]
            max_right.append(right)
        max_right.reverse()
        for j in range(len(height)):
            total_area += min(max_left[j], max_right[j]) - height[j]
        return total_area
