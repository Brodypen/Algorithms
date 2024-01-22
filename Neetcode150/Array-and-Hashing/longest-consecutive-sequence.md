---
status: 
tags:
  - review
  - LC_Medium
<<<<<<< HEAD
sr-due: 2024-02-26
sr-interval: 116
sr-ease: 270
=======
sr-due: 2023-10-17
sr-interval: 11
sr-ease: 250
>>>>>>> bb03e4309c6f95682137ca92f8eb9d23b4ace0e5
---


# Longest Consecutive Sequence
```ad-tldr
title: Summary
collapse: closed
- Put the nums into a set
- If there is no *left neighbor* (No number to the left of it on a numberline), then that means it the start of the sequence.
- Count the sequence by traversing right in the set.
- Result is the max of these counts.
```
## How to solve

This problem is solved by:



### Solution
```ad-tldr
title: Solution
collapse: closed

# New solution
```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Use set, if there is no number to the left, then count. Return max.

        longestConSeq = 0
        numberLine = set(nums)
        
        for n in numberLine:
            if (n-1 not in numberLine):
                count = 1
                while n + count in numberLine:
                    count += 1
                longestConSeq = max(longestConSeq, count)

        return longestConSeq
```


---
##### Cue Flashcards 🗃

---
# References
1. https://leetcode.com/problems/longest-consecutive-sequence/

