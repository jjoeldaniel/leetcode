class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = 1
        zero_product = 1
        res = []
        zeroes = []

        for x in nums:
            if x != 0:
                zero_product *= x
            else:
                zeroes.append(x)

            total_product *= x

        for x in nums:
            # if x is the only zero
            if x == 0:
                if len(zeroes) > 1:
                    res.append(0)
                else:
                    res.append(zero_product)

            # if there are no zeroes
            else:
                res.append(int(total_product / x))

        return res
