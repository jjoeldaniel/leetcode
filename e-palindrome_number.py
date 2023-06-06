class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x)[0] == "-":
            return False
        return str(x) == str(x)[::-1]
