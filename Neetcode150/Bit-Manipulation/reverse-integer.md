---
status: 
tags:
---

# Problem name
```ad-tldr
title: Psuedo Solution
collapse: closed
- First point
- Second point
```
## Problem statement


### Solution
```ad-tldr
title: Solution
collapse: closed

```python
class Solution:
    def reverse(self, x: int) -> int:
        MAX = pow(2, 31)-1
        MIN = pow(-2, 31)

        res = 0
        while x:
            digit = int(math.fmod(x, 10))  # (python dumb) -1 %  10 = 9
            x = int(x / 10)  # (python dumb) -1 // 10 = -1

            if res > MAX // 10 or (res == MAX // 10 and digit > MAX % 10):
                return 0
            if res < MIN // 10 or (res == MIN // 10 and digit < MIN % 10):
                return 0
            res = (res * 10) + digit
        return res

```

---
##### Cue Flashcards 🗃

---
# References
1. 

