---
status: 
tags:
  - LC_Easy
  - review
---

# Problem name
```ad-tldr
title: Psuedo Solution
collapse: closed
- First point
- Second point
```
## Problem statement
Loop through the unsigned integer, and if it a setbit add that value to res at it's reversed position.

### Solution
```ad-tldr
title: Solution
collapse: closed

```python
class Solution:
    def reverseBits(self, n: int) -> int:
        # Check lsb, by shifting right, if bit is set add that value as if it was reversed.
        # Return res.
        res = 0
        
        for i in range(32):
            bit = (n >> i) & 1
            res = res | (bit << (31 - i))
        return res    

```

---
##### Cue Flashcards 🗃

---
# References
1. 

