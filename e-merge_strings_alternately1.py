class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_word = ""

        # get longer length
        if len(word1) > len(word2):
            for i in range(0, len(word1)):

                # only add elements that exist
                if i < len(word1):
                    merged_word += word1[i]
                if i < len(word2):
                    merged_word += word2[i]
        else:
            for i in range(0, len(word2)):

                # only add elements that exist
                if i < len(word1):
                    merged_word += word1[i]
                if i < len(word2):
                    merged_word += word2[i]

        return merged_word
