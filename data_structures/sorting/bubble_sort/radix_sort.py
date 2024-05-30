def get_max_digit_count(numbers):
    """Returns the maximum number of digits in the largest number."""
    max_number = max(numbers)
    return len(str(max_number))

def get_digit(number, digit_index):
    """Returns the digit at digit_index from right (0-based index)."""
    return (number // (10 ** digit_index)) % 10

def counting_sort_by_digit(numbers, digit_index):
    """Performs counting sort on the numbers based on the specified digit index."""
    # Initialize buckets for each digit (0-9)
    buckets = [[] for _ in range(10)]
    
    # Place each number in the appropriate bucket
    for number in numbers:
        digit = get_digit(number, digit_index)
        buckets[digit].append(number)
    
    # Flatten the list of buckets
    sorted_numbers = []
    for bucket in buckets:
        sorted_numbers.extend(bucket)
    
    return sorted_numbers

def radix_sort(numbers):
    """Sorts a list of numbers using Radix Sort."""
    max_digit_count = get_max_digit_count(numbers)
    
    for digit_index in range(max_digit_count):
        numbers = counting_sort_by_digit(numbers, digit_index)
    
    return numbers

# Example usage:
numbers = [170, 45, 75, 90, 802, 24, 2, 66]
sorted_numbers = radix_sort(numbers)
print("Sorted numbers:", sorted_numbers)
