---
status: 
tags:
  - "#review"
  - "#LC_Medium"
sr-due: 2023-09-28
sr-interval: 1
sr-ease: 230
---

<mark style="background: #FF5582A6;">Next review: Do neetcode flash cards and summary</mark>

# Group Anagrams
```ad-tldr
title: Summary
collapse: closed
- First point
- Second point
```
## How to solve

This problem is solved by:
Using a hashmap, with a key : value where the key is the anagram value and value is the the array of anagrams.
The key as the anagram value is an array counter of letters, we have to use a tuple to put in array into the hashMap. tuple(count)

For example:
["eat","tea","tan","ate","nat","bat"]
Key : value
[0,1]... : ['bat']
... : ["nat","tan"]
... : ["ate","eat","tea"]
### Solution
```ad-tldr
title: Solution
collapse: closed

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # What are possible solution?
        # So to find an anagram, we can use a hashmap.
        # If they have the same, we can put them into the same list.
        # # Hashmap
        # # key: value
        # # wordCounter: [word array]
        hashMap = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c)-ord('a')] += 1
            hashMap[tuple(count)].append(s)

        return hashMap.values()
        # What to learn?
        # ord is important.
        # tuple is interesting, since we want to hash a list, have to make it a tuple
        

```

---
##### Cue Flashcards 🗃

---
# References
1. https://leetcode.com/problems/group-anagrams/description/

