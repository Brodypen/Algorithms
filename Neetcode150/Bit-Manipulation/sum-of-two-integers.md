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

Carry bit with & and left shift by one
a ^ b xor to find the actual number in that spot.



### Solution
```ad-tldr
title: Solution
collapse: closed

```python
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff

        while (b & mask) > 0:
            
            carry = ( a & b ) << 1
            a = (a ^ b) 
            b = carry
        
        # handles overflow
        return (a & mask) if b > 0 else a
        

```

---
##### Cue Flashcards 🗃

---
# References
1. 

