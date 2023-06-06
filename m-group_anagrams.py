class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for s in strs:
            # array for each letter in alphabet
            # (question limits us to a-z)
            #
            # each index will correspond with the
            # frequency of the character
            count = [0] * 26

            for c in s:
                # we subtract "a" to start
                # with a 0 index
                count[ord(c) - ord("a")] += 1

            d[tuple(count)].append(s)

        return d.values()
