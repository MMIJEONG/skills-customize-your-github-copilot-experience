# Search and Sort Algorithms


def linear_search(values, target):
    """Return the index of target, or -1 when target is not found."""
    pass


def binary_search(values, target):
    """Search a sorted list and return the index of target, or -1."""
    pass


def selection_sort(values):
    """Return a sorted copy of values without changing the original list."""
    pass


numbers = [42, 7, 19, 3, 25, 11]

# Test linear search.
print("Linear search:", linear_search(numbers, 19))
print("Missing value:", linear_search(numbers, 100))

# Test binary search with a sorted list.
sorted_numbers = sorted(numbers)
print("Binary search:", binary_search(sorted_numbers, 19))
print("Missing value:", binary_search(sorted_numbers, 100))

# Test selection sort without changing numbers.
sorted_copy = selection_sort(numbers)
print("Sorted copy:", sorted_copy)
print("Original list:", numbers)
