
# Canonical pattern:
One Pass
```python
ans = 0
# loop
for x in nums:
    # update ans/state
    pass
return ans
```

Two Passes (Prefix/suffic style)
```python
prefix = [0]*(n+1)
for i in range(n):
    prefix[i+1] = prefix[i] + nums[i]
```


# Problem intuition:
## Problem 2 — slow/fast pointer
Time: O(n) — one pass through the array. Space: O(1) — modified in-place, no extra structures.
You have two pointers both starting at the left, but moving at different speeds. The fast one scans every element, the slow one only advances when it finds something new. The slow pointer always points to where the next unique value should be written. This is the pattern any time you need to modify an array in-place without using extra space.

## Problem 3 — inward scan with skipping
Time: O(n) — each character visited at most once. Space: O(1) — no copy of the string needed if you use pointers directly.
Both pointers start at opposite ends and move toward each other, but instead of comparing values to a target sum they compare characters. The twist is that you skip over anything that isn't a letter or number. You stop as soon as they cross — if every comparison matched, it's a palindrome.

## Problem 4 — greedy pointer movement
Time: O(n) — one pass. Space: O(1) — just tracking a max variable.
Both pointers start at opposite ends like problem 1, but instead of looking for a sum you're maximising an area. The key insight is the decision rule: always move the pointer on the shorter line inward, because the shorter line is the bottleneck. Moving the taller one can never increase the area — the width shrinks and the height is still limited by the short line.

## Problem 5 — two pointers inside an outer loop
Time: O(n²) — O(n log n) for the sort plus O(n²) for the nested scan, so O(n²) overall. Space: O(1) excluding the output list.
This is problem 1 nested inside a regular for loop. You fix one element with the outer loop, then run the full two pointer approach on everything to its right to find pairs that complete the triplet. The tricky part is skipping duplicate values at both the outer and inner level so you don't return the same triplet twice.

## Problem 6 — three pointers simultaneously
Time: O(n) — single pass. Space: O(1) — fully in-place.
Instead of two pointers you have three: low, mid, and high. low marks where the next 0 should go, high marks where the next 2 should go, and mid is the one actually scanning forward. When mid sees a 0 it swaps it to the low end, when it sees a 2 it swaps to the high end, when it sees a 1 it just moves on. You stop when mid and high cross.