class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        res = 0

        for i in range(0, len(flowerbed)):
            if flowerbed[i] == 1:
                continue

            # if 1 element array
            if len(flowerbed) == 1:
                if flowerbed[i] == 1:
                    return 0 == n
                return 1 >= n
            # if normal middle element
            if i > 0 and i != len(flowerbed) - 1:
                if flowerbed[i - 1] != 1 and flowerbed[i + 1] != 1:
                    res += 1
                    flowerbed[i] = 1
            # if start element
            elif i == 0:
                if flowerbed[i + 1] != 1:
                    res += 1
                    flowerbed[i] = 1
            # if end element
            elif i == len(flowerbed) - 1:
                if flowerbed[i - 1] == 0:
                    res += 1
                    flowerbed[i] = 1

        return res >= n
