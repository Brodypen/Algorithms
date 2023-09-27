---
status: 
tags:
  - review
  - LC_Easy
sr-due: 2023-10-01
sr-interval: 4
sr-ease: 270
---

Next review: Do neetcode flash cards.

Two Sum
```ad-tldr
title: Summary
collapse: closed
- First point
- Second point
```
## How to solve

This problem is solved by:
Use a Hash-map, put val: index of nums. Find if it already exists by getting the diff and using that to see in the key exists in the hashMap

### Solution
```ad-tldr
title: Solution
collapse: closed

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hashmap question, put value: position
        hashMap = {}
        for index, n in enumerate(nums):
            # Could also make diff = target - n
            if (target-n) in hashMap:
                return [hashMap[target-n], index]
            hashMap[n] = index
        return 
```

---
##### Cue Flashcards 🗃

---
# References
1. https://leetcode.com/problems/two-sum/

