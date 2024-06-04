from typing import List


def binary_search(numbers: List[int], target: int) -> int:
    low = 0
    high = len(numbers) - 1
    while high >= low:
        mid = int((low + high) / 2)
        if target == numbers[mid]:
            return mid
        elif target < numbers[mid]:
            high = mid - 1
        elif target > numbers[mid]:
            low = mid + 1
    return -1
