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
#   nums   = [1, 3, 5, 7, 9, 11, 14, 18]
#   target = 18
#   output = (2, 6)  because nums[2]=5 and nums[6]=14
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
 
# --- tests ---
if __name__ == "__main__":
    test_two_sum_sorted()
    test_remove_duplicates()
    print("All tests passed!")
 