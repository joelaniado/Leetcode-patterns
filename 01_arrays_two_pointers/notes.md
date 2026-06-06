
# Two Pointer — Arrays: Core Patterns
 
---
 
## Mental Model
 
Two pointers work by **shrinking a search window** from both ends.
Every iteration must move at least one pointer — if nothing moves, you have an infinite loop.
Always ask: *what does each pointer represent, and what shrinks the window?*
 
---
 
## 1. Uniqueness in Arrays
 
**Problem:** find unique elements in a flat or nested array.
 
**Key insight:** sets require hashable types. Lists are mutable → not hashable.
 
```python
# Flat array — O(n) time, O(n) space
unique = list(set(arr))
 
# Nested array — convert inner lists to tuples first
unique = [list(x) for x in set(tuple(i) for i in arr)]
# Time: O(n * k)  where k = length of inner array
# Space: O(n * k)
 
# Never use this — O(n²)
unique = [x for i, x in enumerate(arr) if x not in arr[:i]]
```
 
**Watch out:** `numpy.unique()` sorts first → O(n log n), not O(n).
 
---
 
## 2. Two Sum (Sorted Array)
 
**Problem:** find two numbers that sum to a target.
 
**Pattern:** left starts at 0, right starts at end. Move inward based on sum.
 
```python
def two_sum(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        s = nums[left] + nums[right]
        if s == target:
            return [left, right]
        elif s < target:
            left += 1
        else:
            right -= 1
```
 
**Complexity:** O(n) time | O(1) space
**Requires:** sorted input. If unsorted → sort first O(n log n) or use hashmap O(n).
 
---
 
## 3. Three Sum
 
**Problem:** find all unique triplets that sum to zero.
 
**Pattern:** fix one element with outer loop, run two-pointer two sum on the rest.
Think of it as: *2Sum on a sorted array, repeated n times.*
 
```python
def three_sum(nums):
    nums.sort()
    triplets = []
 
    for i in range(len(nums) - 2):
        # skip duplicate fixed values
        if i > 0 and nums[i] == nums[i - 1]:
            continue
 
        left, right = i + 1, len(nums) - 1
        while left < right:
            check_sum = nums[i] + nums[left] + nums[right]
 
            if check_sum < 0:
                left += 1
            elif check_sum > 0:
                right -= 1
            else:
                triplets.append([nums[i], nums[left], nums[right]])
                # skip duplicates ONLY after a match
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
 
    return triplets
```
 
**Complexity:** O(n log n) sort + O(n²) loop = **O(n²)** time | O(1) space
 
**The three jobs of the inner while loop:**
| sum | action |
|---|---|
| too small | left++ |
| too big | right-- |
| zero | append, skip dupes, move both |
 
**Common bugs:**
- Mixing duplicate skipping into `if/elif` conditions — keep it inside the `else` branch only
- Breaking after first match — there may be multiple valid pairs per fixed element
- Forgetting to advance both pointers after a match → infinite loop
---
 
## 4. Array Uniqueness — Nested (Big O Deep Dive)
 
| Approach | Time | Space | Notes |
|---|---|---|---|
| `set()` flat | O(n) | O(n) | lists not hashable |
| `set(tuple())` nested | O(n·k) | O(n·k) | k = inner length |
| `numpy.unique()` | O(n log n) | O(n) | sorts first |
| Brute force `not in` | O(n²) | O(1) | never use |
 
**Why lists aren't hashable:** lists are mutable. Python refuses to hash mutable objects because the hash could change, breaking set/dict invariants. Tuples are immutable → hashable.
 
---
 
## 5. Dutch National Flag (Sort Colors)
 
**Problem:** sort array of 0s, 1s, 2s in-place in one pass.
 
**Pattern:** three pointers — low, mid, high. Mid scans forward, 
low tracks end of 0-region, high tracks start of 2-region.
 
```python
def sort_colors(nums):
    low, mid, high = 0, 0, len(nums) - 1
 
    while mid <= high:
        if nums[mid] == 0:
            nums[mid], nums[low] = nums[low], nums[mid]
            low += 1
            mid += 1       # safe — low region already processed
        elif nums[mid] == 1:
            mid += 1
        else:              # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
            # do NOT mid++ — incoming value from high is unknown
 
```
 
**Complexity:** O(n) time | O(1) space
 
**The three regions:**
```
[ 0s | 1s | unsorted | 2s ]
       ^low  ^mid      ^high
```
 
**Why it's O(n) even when mid stalls:**
Every iteration shrinks the unsorted region by 1 — either `mid` advances (left shrink) or `high` retreats (right shrink). They can only move toward each other → at most n iterations total.
 
**Why mid doesn't advance after swapping with high:**
The value coming from `high` is unknown — it hasn't been examined yet. After swapping with `low`, the incoming value was already in the processed region, so it's safe to advance.
 
 
## Universal Two Pointer Checklist
 
Before writing any two pointer solution, answer these:
 
1. **Does the array need to be sorted?** If yes, sort first (adds O(n log n))
2. **Where do pointers start?** (both ends vs one fixed + two moving)
3. **What moves each pointer?** (one condition per pointer — keep them independent)
4. **What's the termination condition?** (`left < right` or `mid <= high`)
5. **Are there duplicates to handle?** Skip AFTER processing, not before
6. **Does every iteration shrink the window?** If not, you have an infinite loop
---
 
## Complexity Cheat Sheet
 
| Problem | Time | Space |
|---|---|---|
| Unique flat array | O(n) | O(n) |
| Unique nested array | O(n·k) | O(n·k) |
| Two Sum (sorted) | O(n) | O(1) |
| Three Sum | O(n²) | O(1) |
| Dutch National Flag | O(n) | O(1) |
| Python swap | O(1) | O(1) |