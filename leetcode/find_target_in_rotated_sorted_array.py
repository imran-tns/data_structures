from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1

        if nums[0] > nums[len(nums) - 1]:
            curr_min = float('inf')
            pivot_index = 0
            while start < end:
                mid = start + (end - start) // 2
                if curr_min > nums[mid]:
                    curr_min = nums[mid]
                    pivot_index = mid

                # right has the min
                if nums[mid] > nums[end]:
                    start = mid + 1

                # left has the  min
                else:
                    end = mid - 1

            if curr_min > nums[start]:
                pivot_index = start

            if nums[0] <= target <= nums[pivot_index - 1]:
                start, end = 0, pivot_index - 1
            else:
                start, end = pivot_index, len(nums) - 1

        while start <= end:
            mid = start + (end - start) // 2
            if target > nums[mid]:
                start = mid + 1
            elif target < nums[mid]:
                end = mid - 1
            else:
                return mid
        return -1
