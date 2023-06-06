class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m = defaultdict(int)
        for i in magazine:
            m[i] += 1

        for i in ransomNote:
            if i not in m or m[i] < 1:
                return False

            m[i] -= 1

        return True
