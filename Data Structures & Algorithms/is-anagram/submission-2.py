class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list_one = sorted(s)
        list_two = sorted(t)
        my_dict = {}
        if len(list_one) != len(list_two):
            return False
        else:
            for i in range(len(list_one)):
                if list_one[i] != list_two[i]:
                    return False
            return True