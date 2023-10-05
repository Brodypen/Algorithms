---
status: 
tags:
  - LC_Medium
sr-due: 2023-10-06
sr-interval: 1
sr-ease: 210
---

# Three Sum
```ad-tldr
title: Psuedo Solution
collapse: closed
- One pointer, looping left to right. Skip if it is the same number.
- Two pointers on the other two numbers.
	- if sum < 0: move right, if sum > 0: move left.
	- else, append result, l+=1, r-=1, while nums[l] == nums[l-1] and l < r: l+=1
```
## Problem statement


### Solution
```ad-tldr
title: Solution
collapse: closed

```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                        
        return res


```

---
##### Cue Flashcards 🗃

---
# References
1. 

