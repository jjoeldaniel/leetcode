class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        vals = set()
        for i in nums:
            if i in vals:
                return True
            else:
                vals.add(i)
