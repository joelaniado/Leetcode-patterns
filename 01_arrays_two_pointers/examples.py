# Pattern: Two Pointers
# ---------------------------------------------------------
# Works on SORTED arrays. Place one pointer at each end and
# move them inward based on whether the current sum is too
# high or too low.
#
# Time: O(n)  |  Space: O(1)
# ---------------------------------------------------------

# ==========================================================
# 1. Two sum (sorter array)
# Problem: given a sorted list and a target, return the
# indices of the two numbers that add up to the target.
# Return None if no pair exists.
#
# Example:
#   nums   = [1, 3, 5, 7, 9, 11, 13, 18]
#   target = 18
#   output = (2, 6)  because nums[2]=5 and nums[6]=13
# ============================================================
def two_sum_sorted(nums: list[int], target: int) -> tuple[int, int] | None:
    left, right = 0, len(nums)-1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return (left, right)    
        elif current_sum < target:
            left += 1
        else:
            right -= 1
            
    return None

def test_two_sum_sorted():
    assert two_sum_sorted([1, 3, 5, 7, 9, 11, 14, 18], 18) == (3, 5)
    assert two_sum_sorted([1, 3, 5, 7, 9, 11, 14, 18], 19) == (0, 7)
    assert two_sum_sorted([1, 3, 5, 7, 9, 11, 14, 18], 100) is None
    assert two_sum_sorted([2, 8], 10) == (0, 1)

# =============================================================
# 2. Remove duplicates (sorted array, in-place)
# Problem: given a sorted array, remove duplicates in-place
# and return the number of unique elements. The first k
# elements of nums should hold the unique values in order.
#
# Example:
#   nums   = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
#   output = 5  (first 5 elements become [0, 1, 2, 3, 4])
#
# Hint: use a slow pointer to track the insertion position
# and a fast pointer to scan ahead.
# =============================================================
 
def remove_duplicates(nums: list[int]) -> int:
    left, right = 0, 0
    k = 0
    n = len(nums)
    if n > 0:
        k+=1
    while right < n:
        if nums[left] != nums[right]:
            k += 1
            left += 1
            nums[left] = nums[right]
        right += 1 
    nums = nums[:k]
    return k


 
 
def test_remove_duplicates():
    nums = [1, 1, 2]
    assert remove_duplicates(nums) == 2
 
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    assert remove_duplicates(nums) == 5
 
    # single element — already unique
    nums = [1]
    assert remove_duplicates(nums) == 1
 
    # all duplicates
    nums = [1, 1, 1]
    assert remove_duplicates(nums) == 1

# =============================================================
# 3. Valid palindrome
# Problem: given a string, return True if it reads the same
# forwards and backwards after keeping only alphanumeric
# characters and lowercasing everything.
#
# Example:
#   s = "A man a plan a canal Panama"
#   output = True   ("amanaplanacanalpanama")
#
#   s = "hello"
#   output = False
#
# Hint: use two pointers moving inward, skipping non-
# alphanumeric characters.
# =============================================================
 
def is_palindrome(s: str) -> bool:
    pass  # your code here
 
 
def test_is_palindrome():
    assert is_palindrome("racecar") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("A man a plan a canal Panama") == True
 
    # edge cases
    assert is_palindrome("") == True       # empty string
    assert is_palindrome(" ") == True      # only non-alphanumeric
 
 
# =============================================================
# 4. Container with most water
# Problem: given a list of heights representing vertical lines,
# find the two lines that together with the x-axis form a
# container that holds the most water. Return the max area.
#
# Area = min(heights[left], heights[right]) * (right - left)
#
# Example:
#   heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
#   output  = 49  (lines at index 1 and 8: min(8,7) * 7 = 49)
#
# Hint: always move the pointer with the shorter line inward —
# moving the taller one can only decrease the area.
# =============================================================
 
def max_water(heights: list[int]) -> int:
    pass  # your code here
 
 
def test_max_water():
    assert max_water([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert max_water([4, 3, 2, 1, 4]) == 16   # min(4,4) * 4
    assert max_water([1, 2, 1]) == 2           # min(1,1) * 2
 
    # edge case: only two lines
    assert max_water([1, 1]) == 1
 
 
# =============================================================
# 5. Three sum
# Problem: given a list of integers, return all unique triplets
# [a, b, c] such that a + b + c == 0. The solution must not
# contain duplicate triplets.
#
# Example:
#   nums   = [-1, 0, 1, 2, -1, -4]
#   output = [[-1, -1, 2], [-1, 0, 1]]
#
# Hint: sort first, then fix one element and use two pointers
# on the remainder. Skip duplicates carefully.
# =============================================================
 
def three_sum(nums: list[int]) -> list[list[int]]:
    pass  # your code here
 
 
def test_three_sum():
    assert sorted(three_sum([-1, 0, 1, 2, -1, -4])) == sorted([[-1, -1, 2], [-1, 0, 1]])
    assert three_sum([0, 0, 0]) == [[0, 0, 0]]
    assert three_sum([-2, 0, 0, 2, 2]) == [[-2, 0, 2]]
 
    # no valid triplets
    assert three_sum([1, 2, 3]) == []
 
 
# =============================================================
# 6. Sort colors (Dutch national flag)
# Problem: given a list containing only 0s, 1s, and 2s, sort
# it in-place in a single pass without using Python's sort().
#
# Example:
#   nums   = [2, 0, 2, 1, 1, 0]
#   output = [0, 0, 1, 1, 2, 2]
#
# Hint: use three pointers — low, mid, and high. low tracks
# the boundary of 0s, high tracks the boundary of 2s, and
# mid scans forward.
# =============================================================
 
def sort_colors(nums: list[int]) -> None:
    pass  # your code here (modifies nums in-place, returns None)
 
 
def test_sort_colors():
    nums = [2, 0, 2, 1, 1, 0]
    sort_colors(nums)
    assert nums == [0, 0, 1, 1, 2, 2]
 
    nums = [2, 0, 1]
    sort_colors(nums)
    assert nums == [0, 1, 2]
 
    # edge cases: single element
    nums = [0]
    sort_colors(nums)
    assert nums == [0]
 
    nums = [1]
    sort_colors(nums)
    assert nums == [1]
 
    # all same
    nums = [2, 2, 2]
    sort_colors(nums)
    assert nums == [2, 2, 2]
 
 
# --- run all tests ---
if __name__ == "__main__":
    #test_two_sum_sorted()
    test_remove_duplicates()
    #test_is_palindrome()
    #test_max_water()
    #test_three_sum()
    #test_sort_colors()
    print("\nAll tests passed!\n")
