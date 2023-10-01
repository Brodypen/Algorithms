---
status: 
tags:
  - review
  - LC_Easy
sr-due: 2023-10-16
sr-interval: 15
sr-ease: 290
---

Next review: Do neetcode flash cards.

Two Sum
```ad-tldr
title: Summary
collapse: closed
- Use a hashMap
	- Key: n : Value = index of n
- If that exists in the hashMap
	- return [index of n (hashMap[target-n], currentIndex]
- If not, then add that value into the hashMap.
```
## How to solve

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
	def otherTwoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for index in range(len(nums)):
            if nums[index] in hashMap:
                return [index, hashMap[nums[index]]]
            hashMap[target - nums[index]] = index
```

---
##### Cue Flashcards 🗃

---
# References
1. https://leetcode.com/problems/two-sum/

