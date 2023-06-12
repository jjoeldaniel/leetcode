class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        m = defaultdict(int)
        res = set()
        target = floor(len(nums) / 3)

        for i in nums:
            if m[i] + 1 > target and i not in res:
                res.add(i)
            else:
                m[i] += 1

        return res
