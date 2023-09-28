---
status: 
tags:
  - review
  - LC_Medium
sr-due: 2023-09-29
sr-interval: 1
sr-ease: 230
---

<mark style="background: #FF5582A6;">Next review: Do neetcode flash cards.</mark>

# Problem name
```ad-tldr
title: Summary
collapse: closed
- First point
- Second point
```
## How to solve

This problem is solved by:
Use a hashmap for counter
Make a pseudo sort array, where the index is count(val), val is [val...] and the size is nums length.
Loop reverse and append it to result array, once res array is full, return res.

### Solution
```ad-tldr
title: Solution
collapse: closed

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Array solution, make an array the size of list.
        # IF array, has the count of 1, put it in nums[0], count of 2? nums[1]

        # Not good, this needs it to be sorted. See solution.
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
```

---
##### Cue Flashcards 🗃

---
# References
1. 

