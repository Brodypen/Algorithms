---
status: 
tags:
  - LC_Easy
  - Linked-List
  - NeetCode150
companies: 
Link: https://leetcode.com/problems/linked-list-cycle/description/
---

Timer for 10
Finished in four
# Problem statement
Detect cycle and return true or false if cycle exists
### Solution (Optimized)
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if not head:
            return False
        
        dummyNode = ListNode()
        dummyNode.next= head
        fast, slow = head, dummyNode
        while fast.next and fast.next.next:
            if(fast.val == slow.val):
                return True
            fast = fast.next.next
            slow = slow.next

            
        return False
# Less complicated code I prefer more.
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
    
        fast = head
        slow = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            if fast == slow:
                return True
    
        return False
```
### Notes
While loop for fast and slow should jjust be while fast and fast.next
This will deal withthe not head issue if u just check while fast
Do not need a dummy node, since fast and slow should just start at head and you check if fast == slow after stepping