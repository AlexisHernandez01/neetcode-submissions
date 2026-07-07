class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        # create a freqeuncy counter (dictionary) and iterate
        # through its keys until you find the one that has a 
        # value greater than n/2

        my_dict = {}
        nums_length = len(nums)
        majority_element_size = nums_length/2

        for i in range(nums_length):
            if nums[i] in my_dict:
                my_dict[nums[i]] += 1
            else:
                my_dict[nums[i]] = 1
        
        for key in my_dict.keys():
            if my_dict[key] >= majority_element_size:
                return key
