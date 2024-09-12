---
status: 
tags:
  - LC_Medium
sr-due: 2024-06-01
sr-interval: 31
sr-ease: 230
---

<mark style="background: #FF5582A6;">Next review: Do neetcode flash cards.</mark>
Last review: Couldnt do it but I understodo and figured out the method. Please fix the code.
# Product of Array except Self
```ad-tldr
title: Summary
collapse: closed
- First point
- Second point
```
## How to solve

This problem is solved by:
- I.et [1,2,3,4]  = [24, 12, 8, 6]. You get each answer by calculating the prefix array and the postfix array.
- Loop left, get the prefix. [1, 2, 6, 24]
- Loop reverse, getting the postfix. [24, 24, 12, 4]
- Answer is index - 1 prefix * index + 1 postfix.  [24, 12, 8, 6]. Ex: To get answer[2], get prefix[1] * postfix[3], 8 = 2 * 4

- For better memory, you don't need a prefix/postfix array. You can just use one array and change in place by calculating the prefix first, then the postfix to get the answer.


### Solution
```ad-tldr
title: Solution
collapse: closed

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Loop left, get prefix. Loop right, get postfix.
        
        arrLeft = [1] * len(nums)

        for index in range(1, len(nums)):
            arrLeft[index] = nums[index-1] * arrLeft[index-1]
        # Reverse loop
        postfix = 1
        for index in range(len(nums) -1, -1, -1):
            arrLeft[index] *= postfix
            postfix *= nums[index]

        return arrLeft
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        # prefix mover
        prefix = 1
        for index, n in enumerate(nums):
            res[index] *= prefix
            prefix *= n
        postfix = 1
        for index, n in reversed(list(enumerate(nums))):
            res[index] *= postfix
            postfix *= n

        return res
        
```


---
##### Cue Flashcards 🗃

---
# References
1. https://leetcode.com/problems/product-of-array-except-self/description/

