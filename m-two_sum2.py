class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        m = {}

        for i, x in enumerate(numbers):
            diff = target - x

            if diff in m:
                res = [i + 1, m[diff] + 1]
                res.sort()
                return res

            m[x] = i
