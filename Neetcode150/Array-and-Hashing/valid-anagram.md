---
status: 
tags:
  - "#review"
  - "#LC_Easy"
sr-due: 2023-09-30
sr-interval: 4
sr-ease: 270
---

Next review: Do neetcode flash cards.
# Contains Duplicate
```ad-tldr
title: Summary
collapse: closed
- First point
- Second point
```
## How to solve

This problem is solved by:
Use two hashMap to count each letter in the word, then compare if both hashMap are equal. If they are, that means they are anagrams.

### Solution
```ad-tldr
title: Solution
collapse: closed

```python

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        # hashMap solution
        # counter Hashmap,
        # One line solution.
        # return Counter(s) == Counter(t)

        # Drawn out without Counter
        hashMapS, hashMapT = {}, {}
        for name, x in zip(s, t):
            hashMapS[name] = hashMapS.get(name, 0) + 1
            hashMapT[x] = hashMapT.get(x, 0) + 1
        return hashMapS == hashMapT
```

---
##### Cue Flashcards 🗃

---
# References
1. https://leetcode.com/problems/valid-anagram/description/

