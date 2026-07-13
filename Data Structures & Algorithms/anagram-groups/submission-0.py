class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        my_dict = {}


        for string in strs:
            count = [0] * 26

            for ch in string:
                count[ord(ch) - ord("a")] += 1
            if tuple(count) not in my_dict:
                my_dict[tuple(count)] = []
            my_dict[tuple(count)].append(string)
        
        return list(my_dict.values())