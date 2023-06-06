class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # number : index
        m = {}

        for i, x in enumerate(nums):
            diff = target - x

            # if found
            if diff in m:
                return [m[diff], i]
            # else add
            else:
                m[x] = i

        return [0, 0]
