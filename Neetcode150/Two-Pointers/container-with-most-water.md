---
status: 
tags:
  - review
  - LC_Medium
sr-due: 2024-04-10
sr-interval: 4
sr-ease: 270
---


<mark style="background: #FF5582A6;">Next review: Do neetcode flash cards.</mark>

# Problem name
```ad-tldr
title: Psuedo Solution
collapse: closed
- l, r, res
- maxWater = min(height[l], height[r]) * (r-l)
- Move pointer on the left or on the right.
```
## Problem statement


### Solution
```ad-tldr
title: Solution
collapse: closed

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0
        while l < r:
            maxWater = min(height[l], height[r]) * (r-l)
            res = max(res,maxWater)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            
        return res

```

---
##### Cue Flashcards 🗃

---
# References
1. https://leetcode.com/problems/container-with-most-water/

