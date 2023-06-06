class Solution:
    def reverse(self, x: int) -> int:
        rev = 0

        if str(x)[0] == "-":
            rev = str(x)[::-1]
            rev = int("-" + rev[0 : len(rev) - 1])
        else:
            rev = int(str(x)[::-1])

        if abs(rev) > 2147483647:
            return 0
        else:
            return rev
