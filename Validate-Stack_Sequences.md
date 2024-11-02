---
tags:
  - LC_Medium
  - Stack
  - Google
  - review
Link: https://leetcode.com/problems/validate-stack-sequences/description/
sr-due: 2024-10-17
sr-interval: 4
sr-ease: 270
---

# Problem name
```ad-tldr
title: Psuedo Solution
collapse: closed
- First point
- Second point
```
## Problem statement

See if pushed and popped array would make sense in a stack.

Concepts questions:
Not a problem that you can use pointers to check if somehing exist, you should just use a stack.

Append to stack every pushed number, and check while stack is not empty + the top of stack is equal to next pop, pop it from stack and increment. 
### Solution (Optimized)
```python
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i = 0

        for n in pushed:
            stack.append(n)
            while stack and i < len(popped) and stack[-1] == popped[i]:
                stack.pop()
                i += 1
        return not stack
        

```

---
##### Cue Flashcards 🗃

---
