---
status: 
tags:
  - LC_Easy
  - review
---

# Problem name
```ad-tldr
title: Psuedo Solution
collapse: closed
- First point
- Second point
```
## Problem statement


### Solution
```ad-tldr
title: Solution
collapse: closed

```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # XOR method,
        # same numbers cancel eachother out. ex: 5^5 = 0.
        # Therefore, since there is one number, we can use XOR to find that number.
        res = 0
        for i in range(len(nums) + 1):
            res ^= i
        for num in nums:
            res ^= num
        return res

        

```

---
##### Cue Flashcards 🗃

---
# References
1. 

