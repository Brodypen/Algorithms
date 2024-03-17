# 100236. Count Substrings Starting and Ending with Given Character

# You are given a string s and a character c. Return the total number of substrings of s that start and end with c.
# class Solution:
#     def countSubstrings(self, s: str, c: str) -> int:
#         l, r = 0, 0
#         count = 0
#         while l < len(s):
#             if s[l] == c:
#                 count+=1
#                 r = l+1
#                 while r < len(s):
#                     if s[r] == c:
#                         count+=1
#                     r +=1
#             l+=1
#         return count
        

S = "o"
C = "d"
print(Solution().countSubstrings(S, C)) # 1, got 2
# This test case added line 11, moving r to l+1.

# Couldnt solve, got a time limit exceeded with unknown test case.

# It says the time complexity might be too inefficient.
# Check later to see correct answer.
