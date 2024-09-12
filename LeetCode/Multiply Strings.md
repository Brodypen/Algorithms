---
status: 
tags:
  - LC_Medium
  - "#Math"
  - review
companies: Two Sigma
Link: https://leetcode.com/problems/multiply-strings/description/
sr-due: 2024-09-12
sr-interval: 1
sr-ease: 230
---

# 43. Multiply Strings
```ad-tldr
title: Psuedo Solution
collapse: closed
- First point
- Second point
```
## Problem statement
Given two strings of numbers, multiply them, without changing the entire string to ints, and return as a string.

### Solution
```ad-tldr
title: Solution
collapse: closed

```python
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        res = [0] * (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]

        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                digit = int(num1[i1]) * int(num2[i2])
                res[i1 + i2] += digit
                res[i1 + i2 + 1] += res[i1 + i2] // 10
                res[i1 + i2] = res[i1 + i2] % 10

        res, beg = res[::-1], 0
        while beg < len(res) and res[beg] == 0:
            beg += 1
        res = map(str, res[beg:])
        return "".join(res)
        

```

---
##### Cue Flashcards 🗃

---
# References
1. 

