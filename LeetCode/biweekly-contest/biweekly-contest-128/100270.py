# You are given a string s. The score of a string is defined as the sum of the absolute difference between the ASCII values of adjacent characters.

class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        for i in range(1, len(s)):
            score += abs(ord(s[i]) - ord(s[i - 1]))
        return score

# x = Solution()
# print(x.scoreOfString("hello")) # 13
# print(x.scoreOfString("zaz")) # 50
