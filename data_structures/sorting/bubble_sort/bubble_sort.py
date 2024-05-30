def bubble_sort(input_array):
    n = len(input_array)
    # Traverse through all elements in the list
    for i in range(n):
        # Last i elements are already in place
        second_range = n - i - 1
        for j in range(0, second_range):
            # Traverse the input_array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            left_item = input_array[j]
            right_item = input_array[j+1]
            if left_item > right_item:
                input_array[j], input_array[j+1] = right_item, left_item
    return input_array

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90, 14, 28, 6]
sorted_arr = bubble_sort(arr)
print("Sorted array is:", sorted_arr)
