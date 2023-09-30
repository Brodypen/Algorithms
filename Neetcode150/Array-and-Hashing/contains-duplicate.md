---
status: 
tags:
  - "#review"
  - LC_Easy
sr-due: 2023-10-15
sr-interval: 15
sr-ease: 290
---

# Contains Duplicate

```ad-tldr
title: Psuedo Solution
collapse: closed
- Putting values into a hashSet
- Return true if it was already in the set.
```


### Solution
```ad-tldr
title: Solution
collapse: closed
```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashSet = set()
        for num in nums:
            if num in hashSet:
                return True
            hashSet.add(num)
        return False
```





---
##### Cue Flashcards 🗃
- How many pairs of elements are there, what is the brute force time?
	- n^2 amount of pairs, therefore O(n^2) brute force time complexity to just compare.
- What data structure can we use to lower this time?
	- A hashSet. This makes the time complexity O(n) with space of O(n)

---
# References
1. https://leetcode.com/problems/contains-duplicate/
