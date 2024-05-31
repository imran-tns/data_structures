def selection_sort(arr_to_sort):
    """Sorts an array using the selection sort algorithm."""
    for i in range(len(arr_to_sort)):
        # Find the minimum element in the unsorted part of the array
        min_idx = find_min_index(arr_to_sort, i)

        # Swap the minimum element with the current element
        swap(arr_to_sort, i, min_idx)

    return arr_to_sort


def find_min_index(arr, start_index):
    """Returns the index of the minimum element in the unsorted part of the array."""
    min_idx = start_index
    for j in range(start_index + 1, len(arr)):
        if arr[j] < arr[min_idx]:
            min_idx = j
    return min_idx


def swap(arr, left_index, right_index):
    """Swaps the elements at indices i and j in the array."""
    arr[left_index], arr[right_index] = arr[right_index], arr[left_index]


# Example usage:
arr = [64, 25, 12, 22, 11]
sorted_arr = selection_sort(arr)
print("Sorted array:", sorted_arr)
