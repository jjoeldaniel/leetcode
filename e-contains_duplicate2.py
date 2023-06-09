class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        m = {}
        i = 0

        while i < len(nums):
            
            # if duplicate key
            if nums[i] in m:
                if i-m[nums[i]] <= k:
                    return True
            
            m[nums[i]] = i
            i += 1
        
        return False
