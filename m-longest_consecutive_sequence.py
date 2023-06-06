class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0

        for i in nums:
            # if start of sequence
            if i - 1 not in nums:
                curr = 1

                # iterate until end of sequence
                k = i
                while k + 1 in nums:
                    curr += 1
                    k += 1

                res = max(res, curr)

        return res
