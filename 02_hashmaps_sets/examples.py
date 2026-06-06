# Hash Maps & Sets
# =============================================================
# When to use:
#   - you need O(1) lookup, insert, or membership check
#   - you need to count frequencies of elements
#   - you need to group elements by a derived key
#   - a nested loop solution exists but you want O(n)
#   - you need to track what you've already seen
#
# Ask yourself:
#   Do I need to remember something about elements I've
#   already visited? If yes, a hash map or set is likely
#   the right tool.
#
# Complexity target:
#   Time:  O(n) — hash map lookup and insert are O(1)
#   Space: O(n) — you're trading space for time
# =============================================================
 
 
# =============================================================
# 1. Two sum (unsorted array)
# Problem: given an unsorted list and a target, return the
# indices of the two numbers that add up to the target.
# Return None if no pair exists.
#
# Example:
#   nums   = [2, 7, 11, 15]
#   target = 9
#   output = (0, 1)  because nums[0]=2 and nums[1]=7
#
# Core concept: store each value and its index as you scan.
# For each new element check if its complement (target - n)
# is already in the map. O(n) instead of O(n²) brute force.
#
# Time: O(n)  |  Space: O(n)
# =============================================================
 
def two_sum(nums: list[int], target: int) -> tuple[int, int] | None:
    hashmap = {}
    for i, n in enumerate(nums):
        check = target - n
        if check in hashmap:
            return (hashmap[check],i)
        hashmap[n] = i
    return None
 
 
def test_two_sum():
    assert two_sum([2, 7, 11, 15], 9) == (0, 1)
    assert two_sum([3, 2, 4], 6) == (1, 2)
    assert two_sum([3, 3], 6) == (0, 1)
 
    # no valid pair
    assert two_sum([1, 2, 3], 100) is None
 
 
# =============================================================
# 2. Contains duplicate
# Problem: given a list of integers, return True if any value
# appears at least twice, False if all elements are distinct.
#
# Example:
#   nums   = [1, 2, 3, 1]
#   output = True
#
# Core concept: a set only stores unique values. If the set is
# smaller than the list, a duplicate was removed — that's your
# answer. Alternatively scan and check membership as you go.
#
# Time: O(n)  |  Space: O(n)
# =============================================================
 
def contains_duplicate(nums: list[int]) -> bool:
    my_set = set()
    for n in nums:
        if n in my_set:
            return True
        else:
            my_set.add(n)
    return False
 
 
def test_contains_duplicate():
    assert contains_duplicate([1, 2, 3, 1]) == True
    assert contains_duplicate([1, 2, 3, 4]) == False
    assert contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True
 
    # edge case: single element can't have a duplicate
    assert contains_duplicate([1]) == False
 
 
# =============================================================
# 3. Valid anagram
# Problem: given two strings s and t, return True if t is an
# anagram of s (same characters, same frequencies).
#
# Example:
#   s = "anagram", t = "nagaram"
#   output = True
#
#   s = "rat", t = "car"
#   output = False
#
# Core concept: count character frequencies in s, then
# decrement for each character in t. If any count goes
# negative, t has a character s doesn't.
#
# Time: O(n)  |  Space: O(1) — at most 26 keys for lowercase
# =============================================================
 
def is_anagram(s: str, t: str) -> bool:
    pass  # your code here
 
 
def test_is_anagram():
    assert is_anagram("anagram", "nagaram") == True
    assert is_anagram("rat", "car") == False
    assert is_anagram("a", "a") == True
 
    # different lengths can't be anagrams
    assert is_anagram("ab", "a") == False
 
    # edge case: empty strings
    assert is_anagram("", "") == True
 
 
# =============================================================
# 4. Group anagrams
# Problem: given a list of strings, group all anagrams
# together and return the groups in any order.
#
# Example:
#   strs   = ["eat", "tea", "tan", "ate", "nat", "bat"]
#   output = [["eat","tea","ate"], ["tan","nat"], ["bat"]]
#
# Core concept: anagrams share the same sorted characters.
# Use the sorted string as a key in a hash map where the
# value is the list of strings that share that key.
#
# Time: O(n * k log k) where k is max string length
# Space: O(n)
# =============================================================
 
def group_anagrams(strs: list[str]) -> list[list[str]]:
    pass  # your code here
 
 
def test_group_anagrams():
    result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    result_sorted = sorted([sorted(g) for g in result])
    expected = sorted([sorted(g) for g in [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]])
    assert result_sorted == expected
 
    # edge cases
    assert group_anagrams([""]) == [[""]]
    assert group_anagrams(["a"]) == [["a"]]
 
 
# =============================================================
# 5. Longest consecutive sequence
# Problem: given an unsorted list of integers, return the
# length of the longest sequence of consecutive integers.
# Must run in O(n).
#
# Example:
#   nums   = [100, 4, 200, 1, 3, 2]
#   output = 4  (sequence: 1, 2, 3, 4)
#
# Core concept: load everything into a set for O(1) lookup.
# Only start counting a sequence from a number that has no
# left neighbour (n-1 not in set) — this avoids redundant
# work and keeps it O(n) overall.
#
# Time: O(n)  |  Space: O(n)
# =============================================================
 
def longest_consecutive(nums: list[int]) -> int:
    pass  # your code here
 
 
def test_longest_consecutive():
    assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4
    assert longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
    assert longest_consecutive([1, 2, 3, 4, 5]) == 5
 
    # edge cases
    assert longest_consecutive([]) == 0
    assert longest_consecutive([1]) == 1
 
 
# --- run all tests ---
if __name__ == "__main__":
    #test_two_sum()
    test_contains_duplicate()
    #test_is_anagram()
    #test_group_anagrams()
    #test_longest_consecutive()
    print("All tests passed!")
 