---
status: 
tags:
  - LC_Easy
sr-due: 2024-05-27
sr-interval: 30
sr-ease: 230
---

# Problem name
```ad-tldr
title: Psuedo Solution
collapse: closed
- Two pointers
- Use these two pointers to check letters, if they are not the same return false
- If they are, keep bring them into the middle. Once l < r, return true.
```
## Problem statement
Notes, check using string.lower()
Use isalnum() to check if it an alphabet/digit.
### Solution
```ad-tldr
title: Solution
collapse: closed

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if(s[l].lower() != s[r].lower()):
                return False
            l+=1
            r-=1
        return True
```

---
##### Cue Flashcards 🗃

---
# References
1. https://leetcode.com/problems/valid-palindrome/

