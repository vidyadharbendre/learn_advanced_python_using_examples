# Two Sum Problem

## Problem Statement

Given an array of integers `arr[]` and an integer `target`:

1. **Variant 1:** Return `YES` if there exist two numbers such that their sum is equal to the target. Otherwise, return `NO`.
2. **Variant 2:** Return indices of the two numbers such that their sum is equal to the target. Otherwise, return `[-1, -1]`.

**Note:** You are not allowed to use the same element twice. Example: If the target is equal to 6 and `num[1] = 3`, then `nums[1] + nums[1] = target` is not a solution.

## Examples

### Example 1

**Input Format:** N = 5, arr[] = {2, 6, 5, 8, 11}, target = 14

**Result:**
- Variant 1: `YES`
- Variant 2: `[1, 3]`

**Explanation:** `arr[1] + arr[3] = 14`. So, the answer is `YES` for the first variant and `[1, 3]` for the second variant.

### Example 2

**Input Format:** N = 5, arr[] = {2, 6, 5, 8, 11}, target = 15

**Result:**
- Variant 1: `NO`
- Variant 2: `[-1, -1]`

**Explanation:** There exist no such two numbers whose sum is equal to the target.

## Approaches

### Brute-force Approach

1. **Function:** `find_two_numbers_bruteforce(arr, target)`
2. **Time Complexity:** O(N^2)
   - The brute-force approach uses a double nested loop to check each pair of elements in the array. For an array of size \( N \), this results in \( N \times (N - 1) / 2 \) comparisons in the worst case, leading to a time complexity of \( O(N^2) \).
3. **Space Complexity:** O(1)
   - The brute-force approach uses a constant amount of extra space, regardless of the size of the input array.

### Optimal Approach

1. **Function:** `find_two_numbers_optimal(arr, target)`
2. **Time Complexity:** O(N)
   - The optimal approach uses a single pass through the array, leveraging a hash map (dictionary) to store and look up the complement values. This results in a linear time complexity of \( O(N) \).
3. **Space Complexity:** O(N)
   - The optimal approach requires extra space to store the hash map, which can contain up to \( N \) entries in the worst case.

## Usage

### Code

```python
def find_two_numbers_bruteforce(arr, target):
    """
    Brute-force approach to find two numbers that sum up to the target.
    Time Complexity: O(N^2)
    Space Complexity: O(1)
    """
    N = len(arr)
    for i in range(N):
        for j in range(i + 1, N):
            if arr[i] + arr[j] == target:
                return "YES", [i + 1, j + 1]  # Convert to 1-based index
    return "NO", [-1, -1]

def find_two_numbers_optimal(arr, target):
    """
    Optimal approach to find two numbers that sum up to the target using a hash map.
    Time Complexity: O(N)
    Space Complexity: O(N)
    """
    index_map = {}
    for i, num in enumerate(arr):
        complement = target - num
        if complement in index_map:
            return "YES", [index_map[complement] + 1, i + 1]  # Convert to 1-based index
        index_map[num] = i
    return "NO", [-1, -1]

def print_results(N, arr, target, method):
    """
    Function to print the results of both brute-force and optimal approaches.
    """
    result_variant1, result_variant2 = method(arr, target)
    print(f"Input Format: N = {N}, arr[] = {arr}, target = {target}")
    print(f"Result: {result_variant1} (for 1st variant)")
    print(f"        {result_variant2} (for 2nd variant)")

# Example 1
N1 = 5
arr1 = [2, 6, 5, 8, 11]
target1 = 14
print("Brute-force Approach:")
print_results(N1, arr1, target1, find_two_numbers_bruteforce)
print("Optimal Approach:")
print_results(N1, arr1, target1, find_two_numbers_optimal)

# Example 2
N2 = 5
arr2 = [2, 6, 5, 8, 11]
target2 = 15
print("Brute-force Approach:")
print_results(N2, arr2, target2, find_two_numbers_bruteforce)
print("Optimal Approach:")
print_results(N2, arr2, target2, find_two_numbers_optimal)
```
