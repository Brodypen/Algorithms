---
status: 
tags:
  - review
  - LC_Medium
sr-due: 2023-10-06
sr-interval: 1
sr-ease: 240
---

<mark style="background: #FF5582A6;">Next review: Do neetcode flash cards.</mark>

# Two sum on a sorted list
```ad-tldr
title: Psuedo Solution
collapse: closed
- Two pointers
- Move left pointer if sum < target
- Move right pointer if sum > target
```
## Problem statement
Two pointers two sum
### Solution
```ad-tldr
title: Solution
collapse: closed

```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Two pointers solution, search to find target.
        l, r = 0, len(numbers) - 1
        while l < r:
            sum = numbers[l] + numbers[r]
            if sum < target:
                l+=1
            elif sum > target:
                r -=1
            elif sum == target:
                return [l+1, r+1]

```

---
##### Cue Flashcards 🗃

---
# References
1. [Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)

