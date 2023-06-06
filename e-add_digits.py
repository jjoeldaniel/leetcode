class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            x = 0
            for i in str(num):
                x += int(i)
            num = x

        return num
