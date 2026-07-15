class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        one, two = 0, 0
        result = ""
        last_index = 0
        short = 0

        if len(word1) < len(word2):
            n = len(word1)
            short = 1
        elif len(word1) > len(word2):
            n = len(word2)
            short = 2
        else:
            n = len(word1)

        for i in range(n):
            result += word1[i]
            result += word2[i]
            last_index = i

        if short == 1:
            result += word2[last_index + 1:len(word2)]
        elif short == 2:
            result += word1[last_index + 1:len(word1)]
        else:
            result = result
        return result
