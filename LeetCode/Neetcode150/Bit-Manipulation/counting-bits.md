---
status: 
tags:
  - LC_Easy
  - review
sr-due: 2024-04-07
sr-interval: 3
sr-ease: 250
---

# Counting bits
```ad-tldr
title: Psuedo Solution
collapse: closed
- First point
- Second point
```
## Problem statement

Use DP to calculate order, answer is MSB-value + dp[1-MSB-index]

### Solution
```ad-tldr
title: Solution
collapse: closed

```python
# class Solution:
    # def countBits(self, n: int) -> List[int]:
    #     # My solution, O(n*setBitsOfI)
    #     ans = []
    #     for i in range(n+1):
    #         countBitsOfI = i
    #         numberOfSetBits = 0
    #         while countBitsOfI:
    #             countBitsOfI &= (countBitsOfI-1)
    #             numberOfSetBits += 1
    #         ans.append(numberOfSetBits)

    #     return ans

    # Neetcode solution, O(n), dp solution
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp
            

```

---
##### Cue Flashcards 🗃

---
# References
1. https://leetcode.com/problems/counting-bits/description/

