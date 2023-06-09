class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        res = []

        for i in nums:
            d[i] += 1

        d = OrderedDict(sorted(d.items(), reverse=True, key=lambda x: x[1]))
        for key in d.keys():
            res.append(key)
            if len(res) == k:
                break

        return res
