---
status: 
tags:
  - review
  - LC_Easy
sr-due: 2024-03-17
sr-interval: 4
sr-ease: 270
---

<mark style="background: #FF5582A6;">Next review: Do neetcode flash cards.</mark>

# Problem name
```ad-tldr
title: Psuedo Solution
collapse: closed
- First point
- Second point
```
## Problem statement
Invert a binary tree and return the root

### Solution
```ad-tldr
title: Solution
collapse: closed

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        self.invertTree(root.left)
        self.invertTree(root.right) 

        root.left, root.right = root.right, root.left
        return root   

```

---
##### Cue Flashcards 🗃

---
# References
1. 

