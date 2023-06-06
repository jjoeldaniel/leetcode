class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""

        for i in s:
            if not str(i).isalnum():
                continue
            else:
                res += str(i).lower()

        return res == res[::-1]
