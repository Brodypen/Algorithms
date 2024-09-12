---
status: 
tags:
  - LC_Easy
sr-due: 2024-04-06
sr-interval: 3
sr-ease: 250
---
# 136. Single Number
```ad-tldr
title: Psuedo Solution
collapse: closed
- First point
- Second point
```
## Problem statement
Find the odd number out in an array filled with pairs
Example nums = [2,2,1] output: 1
### Solution
```ad-tldr
title: Solution
collapse: closed

```python
class Solution:
    # Solution, by using XOR, you can 'subtract' the other pair.
    # 2 = 10, 2 XOR 2 = 00. Does not matter what order you do it as.
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res ^= n
        return res

```

---
##### Cue Flashcards 🗃
Know XOR, ^, how does XOR work
---
# References
1. https://leetcode.com/problems/single-number/

