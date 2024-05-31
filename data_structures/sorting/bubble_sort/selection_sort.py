# def selection_sort(arr):
#     # Traverse through all array elements
#     for i in range(len(arr)):
#         # Find the minimum element in remaining unsorted array
#         min_idx = i
#         for j in range(i+1, len(arr)):
#             if arr[min_idx] > arr[j]:
#                 min_idx = j
        
#         # Swap the found minimum element with the first element
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]

#     return arr

def selection_sort(arr):
    """Sorts an array using the selection sort algorithm."""
    for i in range(len(arr)):
        # Find the minimum element in the unsorted part of the array
        min_idx = find_min_index(arr, i)
        
        # Swap the minimum element with the current element
        swap(arr, i, min_idx)

    return arr

def find_min_index(arr, start_index):
    """Returns the index of the minimum element in the unsorted part of the array."""
    min_idx = start_index
    for j in range(start_index + 1, len(arr)):
        if arr[j] < arr[min_idx]:
            min_idx = j
    return min_idx

def swap(arr, i, j):
    """Swaps the elements at indices i and j in the array."""
    arr[i], arr[j] = arr[j], arr[i]

# Example usage:
arr = [64, 25, 12, 22, 11]
sorted_arr = selection_sort(arr)
print("Sorted array:", sorted_arr)


