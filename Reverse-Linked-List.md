---
status: 
tags:
  - LC_Easy
  - Linked-List
  - NeetCode150
Link: https://leetcode.com/problems/reverse-linked-list/description/
---
Finished in 2 minutes
# Problem name
```ad-tldr
title: Psuedo Solution
collapse: closed
- First point
- Second point
```
## Problem statement

### Solution (Optimized)
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            _next = curr.next
            curr.next = prev
            prev = curr
            curr = _next
        return prev
        

```
