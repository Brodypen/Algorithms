---
status: 
tags:
  - LC_Easy
  - review
sr-due: 2024-05-26
sr-interval: 22
sr-ease: 210
---

<mark style="background: #FF5582A6;">Next review: Do neetcode flash cards.</mark>

# Best time to buy and sell stocks
```ad-tldr
title: Psuedo Solution
collapse: closed
- First point
- Second point
```
## Problem statement
Find max profit in a graph, left to right.



### Solution
```ad-tldr
title: Solution
collapse: closed

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        res = 0
        while (r < len(prices)):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                res = max(profit, res)
            else:
                l = r
            r += 1 
        return res

    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        
        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price
            res = max(res, price - lowest)
        return res

```


---
##### Cue Flashcards 🗃

---
# References
1. 

