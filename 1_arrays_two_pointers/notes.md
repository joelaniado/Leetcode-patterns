
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