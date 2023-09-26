---
status: 
tags:
  - "#review"
sr-due: 2023-09-30
sr-interval: 4
sr-ease: 270
---
Next review: Do neetcode flash cards.
# Contains Duplicate

## How to solve

This problem is solved by:
Putting values into a set, then return true if it was already in the set.

### Solution
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

---
# References
1. https://leetcode.com/problems/contains-duplicate/
