---
status: 
tags:
  - LC_Easy
  - review
sr-due: 2024-04-07
sr-interval: 4
sr-ease: 270
---

# Problem name
```ad-tldr
title: Psuedo Solution
collapse: closed
- First point
- Second point
```
## Problem statement
Count number of set bits.

### Solution
```ad-tldr
title: Solution
collapse: closed

```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        # Brute force: O(n)
        # This solution checks the LSB (right most bit), if 1, increment count.
        # Then rightshift, while n.

        # Optimal solution: O(L) (L => Count of bits that are one)
        # We use n= n&(n-1), this will repeat = to amount of count of bits that are one.
        
        count = 0
        while n:
            n &=(n-1)
            count += 1

        return count
        

```

---
##### Cue Flashcards 🗃

---
# References
1. https://leetcode.com/problems/number-of-1-bits/description/

