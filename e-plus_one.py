class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()
        digits[0] += 1

        for i in range(len(digits)):
            if digits[i] >= 10:

                digits[i] -= 10

                # if final num
                if i == len(digits) - 1: digits.append(1)

                # loop through array and appropriately
                # increment
                else:
                    digits[i+1] += 1
                    for x in range(i+1, len(digits)):

                        # if we no longer need to increment
                        if digits[x] < 10: break
                        else:
                            digits[x] -= 10

                            # if at final value, we have
                            # to create a new index
                            if x+1 > len(digits)-1:
                                digits.append(1)
                            else:
                                digits[x+1] += 1

        digits.reverse()
        return digits
