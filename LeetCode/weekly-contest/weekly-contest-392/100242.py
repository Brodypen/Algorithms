class Solution:
    # DISTANCE SHOULD RETURN minimum distance between string.
    # For example, distance("ab", "cd") == 4, and distance("a", "z") == 1.

    # Fix this code, distance("a", "z") should return 1.
    def getDistanceOfTwoChars(self, c1: str, c2: str) -> int:
        diff = abs(ord(c1) - ord(c2))
        return min(diff, 26 - diff)
    def distance(self, s1: str, s2: str) -> int:
        res = 0
        for i in range(len(s1)):
            res += self.getDistanceOfTwoChars(s1[i], s2[i])
        return res
    def getSmallestString(self, s: str, k: int) -> str:
        newStr = ""
        for i in range(len(s)):
            
        return newStr
x = Solution()

# print(x.distance("ab", "cd")) # 4
# print(x.distance("a", "z")) # 1

print(x.getSmallestString("zbbz", 3), "aaaz")
print(x.getSmallestString("xaxcd", 4), "aawcd") 
print(x.getSmallestString("lol", 0), "lol") 