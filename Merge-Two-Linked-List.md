---
status: 
tags:
  - review
  - LC_Easy
  - Linked-List
  - NeetCode150
Link: 
sr-due: 2024-09-30
sr-interval: 1
sr-ease: 230
---
Couldn't solve it in 10 minutes, watching coding portion and try again.

Okay, finish the actual code after watching for 3 minutes. Only thing missing was curr = curr.next
oops.
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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newList = ListNode()

        curr = newList

        currList1 = list1
        currList2 = list2
        while currList1 and currList2:
            if currList1.val < currList2.val:
                curr.next = currList1
                currList1 = currList1.next
            else:
                curr.next = currList2
                currList2 = currList2.next
            curr = curr.next

        if currList1:
            curr.next = currList1

        if currList2:
            curr.next = currList2

        return newList.next
```
You don't have to make currList1 or 2, if list1 and list2 can be changed.

---
##### Cue Flashcards 🗃

---
