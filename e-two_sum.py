class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # val -> index
        map_vals = {}

        # iterate through list, tracking both
        # the index and value
        for i, n in enumerate(nums):

            # diff is the number which will, when
            # added to n, sum to the target value
            diff = target - n

            # if we hold the answer, we return i &
            # the index value of `diff`
            if diff in map_vals:
                return [map_vals[diff], i]

            # otherwise, we add (k,v) pair
            map_vals[n] = i
