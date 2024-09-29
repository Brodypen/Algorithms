---
status: 
tags:
  - LC_Easy
  - Linked-List
Link: https://leetcode.com/problems/palindrome-linked-list/
---

# Problem name

## Problem statement
Cool problem, usage of [Linked-List-Cycle](Linked-List-Cycle.md) and [Reverse-Linked-List](Reverse-Linked-List.md) to solve this problem.

### Solution

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Get the list in this state where we point to the middle node.
        # [1,2,3,4,5]will be 1->2->3<-4<-5

        # How? Fast and slow pointer to get middle, reverse the right side, then use left and right pointers to return False if val dont match
        # Brute force, use array O(n) memory and time
        # vals = []
        # curr = head
        # while curr:
        #     vals.append(curr.val)
        #     curr = curr.next
        # return vals == vals[::-1]

        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # We got the middle node in slow node. Reverse from theer
        prev = None
        curr = slow
        while curr:
            next_ = curr.next
            curr.next = prev
            prev = curr
            curr = next_
        
        # From here, we have reversed the right side.

        left = head
        right = prev
        # print(left.val, right.val)
        while left and right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next


        return True
              

```

---
##### Cue Flashcards 🗃

---
