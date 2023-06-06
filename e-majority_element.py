class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = defaultdict(int)

        for i in nums:
            m[i] += 1

        freq = 0
        key = 0

        for k, v in m.items():
            if v > freq:
                freq = v
                key = k

        return key
