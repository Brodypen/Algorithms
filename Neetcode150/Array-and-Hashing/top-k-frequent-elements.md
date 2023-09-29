---
status: 
tags:
  - review
  - LC_Medium
sr-due: 2023-10-01
sr-interval: 2
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
Make a pseudo Bucketsort array, where the index is count(val), val is [val...] and the size is nums length.
Loop reverse and append it to result array, once res array is equal to k, return res.

Key notes:
Know to make unique arrays in array, you have to do [[] for i in range(len(nums) + 1)]. If you don't, you are making copies of the array. That means when u change a val in one array, in changes vals in all. (Because it is only one array)

### Solution
```ad-tldr
title: Solution
collapse: closed

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)] # Important

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(nums), 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
```

---
##### Cue Flashcards 🗃

---
# References
1. https://leetcode.com/problems/top-k-frequent-elements/description/

