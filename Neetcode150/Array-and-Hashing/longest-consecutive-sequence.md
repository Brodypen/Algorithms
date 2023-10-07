---
status: 
tags:
  - review
  - LC_Medium
sr-due: 2023-10-17
sr-interval: 11
sr-ease: 250
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

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Method, use a set.
        # If the number does not exist in the left of it, then you will count to the right.
        # This will get your the longest in O(n) time
        numSet = set(nums)
        res = 0
        for n in numSet:
            if (n - 1) not in numSet:
                count = 1
                while(n + count) in numSet:
                    count+=1
                res = max(res, count)
        return res

```

---
##### Cue Flashcards 🗃

---
# References
1. https://leetcode.com/problems/longest-consecutive-sequence/

