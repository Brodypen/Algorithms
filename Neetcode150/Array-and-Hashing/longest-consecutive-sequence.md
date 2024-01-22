---
status: 
tags:
  - review
  - LC_Medium
sr-due: 2024-02-26
sr-interval: 116
sr-ease: 270
---

<mark style="background: #FF5582A6;">Next review: Do neetcode flash cards.</mark>

# Longest Consecutive Sequence
```ad-tldr
title: Summary
collapse: closed
- First point
- Second point
```
## How to solve

This problem is solved by:
- Put the nums into a set
- If there is no *left neighbor* (No number to the left of it on a numberline), then that means it the start of the sequence.
- Count the sequence by traversing right in the set.
- Result is the max of these counts.


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

