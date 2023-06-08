class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        r = 0

        for i in s[::-1]:
            if i == " ":
                if r > 0:
                    break
            else:
                r += 1
    
        return r
