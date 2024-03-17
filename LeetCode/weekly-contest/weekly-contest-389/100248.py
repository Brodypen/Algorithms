# 100248. Existence of a Substring in a String and Its Reverse

class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        # Theory
        # We can use two pointers, in which we check if left matches right substring
#         l, r = 0, len(s) - 1
#         while l < r:
#             print(s[l] + s[l+1])
#             print(s[r-1] + s[r])
#             if(s[l] + s[l+1] == s[r-1] + s[r]):
#                 return True
#             l+=1
#             r-=1
        
#         return False
        # Other method, just put every substring of length 2 in set. check if it exist in set
        subStringSet = set()
        for i in range(len(s)-1):
            subStringSet.add(s[i] + s[i+1])
        # print(subStringSet)
        for i in range(len(s)-1, 0, -1):
            # print(s[i] + s[i-1])
            if(str(s[i] + s[i-1]) in subStringSet):
                return True
        return False

# input = "qg"
# print(Solution().isSubstringPresent(input))
    
# Better solution
# Instead of using set, just have the reverse string.
# Then you check if the substring is in the reverse string.