class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        m = {"}": "{", ")": "(", "]": "["}

        # iterate through each char
        for c in s:
            # if closing
            if c in m:
                if stack and stack[-1] == m[c]:
                    stack.pop()
                else:
                    return False
            # if opening
            else:
                stack.append(c)

        return not stack
