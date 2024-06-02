from data_structures.sorting.bubble_sort.radix_sort import radix_sort


def test_radix_sort():
    # Test case 1: empty array
    assert radix_sort([]) == []

    # Test case 2: single element array
    assert radix_sort([5]) == [5]

    # Test case 3: array already sorted
    assert radix_sort([1, 2, 3]) == [1, 2, 3]

    # Test case 4: array with duplicates
    assert radix_sort([3, 1, 2, 1, 3]) == [1, 1, 2, 3, 3]

    # Test case 5: array with negative numbers
    # assert radix_sort([-5, 2, -10, 1, 0]) == [-10, -5, 0, 1, 2]

    # Test case 6: array with large numbers
    assert radix_sort([1000000000, 1, 2, 3, 1000000001]) == [1, 2, 3, 1000000000, 1000000001]
