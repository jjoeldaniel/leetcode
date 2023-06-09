class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            m = (l+r) // 2

            # lower bound
            if nums[m] > target:
                r = m-1
            # upper bound
            elif nums[m] < target:
                l = m+1
            # base case
            else:
                return m
        return l
