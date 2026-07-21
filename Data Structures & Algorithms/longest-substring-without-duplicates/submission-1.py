class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        curr_length = 0
        window = list()

        for i in range(len(s)):
            
            if s[i] not in window:
                window.append(s[i])
                curr_length += 1
            else:
                index = window.index(s[i])
                window = window[index + 1:]
                window.append(s[i])
                curr_length = len(window)

            max_length = max(max_length, curr_length)
        print(window)
        return max_length