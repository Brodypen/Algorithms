# Clear digits
class Solution:
    def clearDigits(self, s: str) -> str:
        stackWord = []
        for c in s:
            if(c.isdigit()):
                stackWord.pop()
            else:
                stackWord.append(c)
        return ''.join(stackWord)