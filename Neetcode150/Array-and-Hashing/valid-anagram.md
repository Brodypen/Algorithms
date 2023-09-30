---
status: 
tags:
  - "#review"
  - "#LC_Easy"
sr-due: 2023-10-14
sr-interval: 14
sr-ease: 290
---

# Valid Anagrams
```ad-tldr
title: Psuedo Solution
collapse: closed
- Use two hashMap to count each letter in the word
- Key = Letters, values = Count of letter
- compare if both hashMap are equal. 
- If they are, that means they are anagrams.
```


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
- Brute force solution
	- Put into an array, sort them and compare. O(n log n) time
- Keys = Letters, Values = Count of each letters
	- Time complexity is O(n), space is O(n)
---
# References
1. https://leetcode.com/problems/valid-anagram/description/

