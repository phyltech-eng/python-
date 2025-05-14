import random 
import math

def binary_search(arr, target):
    """
    Perform binary search on a sorted array to find the index of the target value.

    Args:
        arr (list): A sorted list of elements.
        target: The value to search for.

    Returns:
        int: The index of the target value in the array, or -1 if not found.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
def generate_sorted_array(size, min_value=0, max_value=100):
    """ 
    Generate a sorted array of unique random integers.

    Args:
        size (int): The size of the array to generate.
        min_value (int): The minimum value in the array.
        max_value (int): The maximum value in the array.

    Returns:

        list: A sorted list of unique random integers.
    """
    if size > (max_value - min_value + 1):
        raise ValueError("Size exceeds the range of unique values.")
    
    arr = random.sample(range(min_value, max_value + 1), size)
    arr.sort()
    return arr
def test_binary_search():
    """
    Test the binary search function with various cases.
    """
    # Test case 1: Basic test
    arr = [1, 2, 3, 4, 5]
    target = 3
    result = binary_search(arr, target)
    assert result == 2, f"Expected index 2, got {result}"

    # Test case 2: Target not in array
    target = 6
    result = binary_search(arr, target)
    assert result == -1, f"Expected -1, got {result}"

    # Test case 3: Empty array
    arr = []
    target = 1
    result = binary_search(arr, target)
    assert result == -1, f"Expected -1, got {result}"

    # Test case 4: Single element array
    arr = [1]
    target = 1
    result = binary_search(arr, target)
    assert result == 0, f"Expected index 0, got {result}"

    # Test case 5: Large array
    size = 1000
    arr = generate_sorted_array(size)
    target = arr[random.randint(0, size - 1)]
    result = binary_search(arr, target)
    assert result != -1, "Target should be found in the array"

    