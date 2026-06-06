
# 01 · Arrays & Two Pointers

## When to use
- Input is sorted or can be sorted without breaking the problem
- You need to find a pair or triplet that meets a condition
- A nested loop O(n²) solution exists and you want to reduce it to O(n)
- You need to modify an array in-place with O(1) space
- The problem involves comparing elements from both ends (palindromes, containers)
- The problem involves partitioning an array into regions

## The core question to ask
> Can I learn something useful by comparing the leftmost and rightmost elements?  
> If moving a pointer in one direction makes the problem more or less solved  
> in a predictable way, two pointers will work.

## When it won't work
- Unsorted array where you need exact pair matches → use a hash map instead
- You need to track a window of elements → use sliding window
- The decision of which pointer to move depends on future elements → use DP

---

## Complexity targets
| Variant | Time | Space |
|---|---|---|
| Single pass (inward or fast/slow) | O(n) | O(1) |
| Nested (e.g. three sum) | O(n²) | O(1) excl. output |

---

## Variants & core concepts

### 1. Opposite end scan — Two sum (sorted)
Start one pointer at each end. Move inward based on whether the
current sum is too high or too low. Works because sorted order
tells you which direction to move.

```python
left, right = 0, len(nums) - 1
while left < right:
    current_sum = nums[left] + nums[right]
    if current_sum == target:
        return (left, right)
    elif current_sum < target:
        left += 1
    else:
        right -= 1
```

---

### 2. Slow / fast pointer — Remove duplicates
Two pointers both start at the left but move at different speeds.
Fast pointer scans every element. Slow pointer only advances when
it finds something new — it marks the next write position.

```python
k = 1
for right in range(1, len(nums)):
    if nums[right] != nums[k - 1]:
        nums[k] = nums[right]
        k += 1
return k
```

---

### 3. Inward scan with skipping — Valid palindrome
Pointers move inward from both ends but skip invalid characters.
Pointers don't have to advance by exactly one step every iteration.
Always guard inner skip loops with `left < right` to avoid index errors.

```python
left, right = 0, len(s) - 1
while left < right:
    while left < right and not s[left].isalnum():
        left += 1
    while left < right and not s[right].isalnum():
        right -= 1
    if s[left].lower() != s[right].lower():
        return False
    left += 1
    right -= 1
return True
```

---

### 4. Greedy pointer movement — Container with most water
Always move the pointer on the shorter line inward. Moving the
taller one shrinks the width without any chance of increasing
height — it can never improve the area. You are not proving the
move will find the best answer; you are proving all remaining
pairs with the shorter line are guaranteed to be worse.

```python
left, right = 0, len(heights) - 1
max_area = 0
while left < right:
    max_area = max(max_area, min(heights[left], heights[right]) * (right - left))
    if heights[left] < heights[right]:
        left += 1
    else:
        right -= 1
return max_area
```

---

### 5. Two pointers inside an outer loop — Three sum
Reduce a three-variable problem to a two-variable problem by
fixing one element with an outer loop, then running two pointers
on the remainder. Must sort first. Skip duplicates at both the
outer level and the inner level after finding a valid triplet.

```python
nums.sort()
result = []
for i in range(len(nums)):
    if i > 0 and nums[i] == nums[i - 1]:
        continue
    left, right = i + 1, len(nums) - 1
    while left < right:
        total = nums[i] + nums[left] + nums[right]
        if total == 0:
            result.append([nums[i], nums[left], nums[right]])
            while left < right and nums[left] == nums[left + 1]:
                left += 1
            while left < right and nums[right] == nums[right - 1]:
                right -= 1
            left += 1
            right -= 1
        elif total < 0:
            left += 1
        else:
            right -= 1
return result
```

---

### 6. Three pointers / partitioning — Sort colors
Three pointers divide the array into regions. `low` marks the
boundary of 0s, `high` marks the boundary of 2s, `mid` scans
forward. Each swap maintains the invariant of each region.
Stop when `mid` and `high` cross. This is the foundation of
quicksort's partition step.

```python
low, mid, high = 0, 0, len(nums) - 1
while mid <= high:
    if nums[mid] == 0:
        nums[low], nums[mid] = nums[mid], nums[low]
        low += 1
        mid += 1
    elif nums[mid] == 1:
        mid += 1
    else:
        nums[mid], nums[high] = nums[high], nums[mid]
        high -= 1
```

---

## Gotchas to remember
- Always guard inner skip loops with a bounds check (`left < right`)
- For three sum: sort first, skip duplicates at both levels
- `pop(i)` is O(n) for any index except the last — avoid in two pointer solutions
- The slow/fast pointer pattern modifies in-place — reassigning the list variable inside the function does nothing to the original
- Equal height case in container with most water: moving either pointer is fine

---

## LeetCode problems to revisit
| Problem | Difficulty | Pattern |
|---|---|---|
| Two Sum II | Easy | Opposite end scan |
| Remove Duplicates from Sorted Array | Easy | Slow / fast pointer |
| Valid Palindrome | Easy | Inward scan with skipping |
| Container With Most Water | Medium | Greedy pointer movement |
| 3Sum | Medium | Two pointers in outer loop |
| Sort Colors | Medium | Three pointer partitioning |