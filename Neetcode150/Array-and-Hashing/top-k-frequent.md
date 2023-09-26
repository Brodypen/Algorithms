---
Status: 
Tags:

---
```ad-tldr
title: Summary
collapse: open
Get top k frequency with hashtable counting frequency, then loop through an array in desc order in adding them into a list until len(list) == k
```

# TopKFrequent


Fastest way is to get frequency count with a hashtable, they put it into an array of lists index by the count.
Then you loop through that array of lists backwards by frequency appending the mostFreq until len(res) == k, then return res.

---

##### Cue Flashcards 🗃
#flashcard

---
# References
1. https://leetcode.com/problems/top-k-frequent-elements/
2. https://www.youtube.com/watch?v=YPTqKIgVk-k 
