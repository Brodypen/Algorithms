---
status: 
tags:
  - LC_Easy
  - review
sr-due: 2023-11-07
sr-interval: 4
sr-ease: 270
---

<mark style="background: #FF5582A6;">Next review: Do neetcode flash cards.</mark>

# Longest substring without repeating chars
```ad-tldr
title: Psuedo Solution
collapse: closed
- First point
- Second point
```
## Problem statement
1. use Hashset, if the char on the right pointer is in the set, slide the left window to the right till it doesnt.

### Solution
```ad-tldr
title: Solution
collapse: closed

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashSet = set()
        l, r = 0, 0
        res = 0
        while r < len(s):

            while s[r] in hashSet:
                hashSet.remove(s[l])
                l += 1
            hashSet.add(s[r])
            r+=1
            res = max(res, r-l)
        return res

```

---
##### Cue Flashcards 🗃

---
# References
1. https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

