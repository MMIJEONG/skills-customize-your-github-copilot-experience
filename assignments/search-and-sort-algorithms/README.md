# 📘 Assignment: Search and Sort Algorithms

## 🎯 Objective

Learn how to find values in lists and arrange values in order by implementing linear search, binary search, and selection sort in Python.

## 📝 Tasks

### 🛠️ Implement Linear Search

#### Description
Write a function that checks each item in a list from left to right until it finds the target value.

#### Requirements
Completed program should:

- Define a function `linear_search(values, target)`
- Return the index of the first matching value
- Return `-1` when the target is not present
- Demonstrate the function with a list that includes both a found and a missing value


### 🛠️ Implement Binary Search

#### Description
Write a function that searches a sorted list by repeatedly checking the middle item and eliminating the half that cannot contain the target.

#### Requirements
Completed program should:

- Define a function `binary_search(values, target)`
- Assume that `values` is already sorted in ascending order
- Return the index of the matching value
- Return `-1` when the target is not present
- Demonstrate the function with at least two targets


### 🛠️ Implement Selection Sort

#### Description
Write a function that repeatedly finds the smallest remaining value and places it in the next position. The function should sort a copy of the input so the original list is unchanged.

#### Requirements
Completed program should:

- Define a function `selection_sort(values)`
- Return a new list sorted in ascending order
- Leave the original input list unchanged
- Demonstrate the function with an unsorted list
- In a short comment or print statement, identify which search method is more efficient for a sorted large list and explain why
