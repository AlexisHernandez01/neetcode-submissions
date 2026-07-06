class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        my_list = []
        nums_len = len(nums)
        
        for i in range(nums_len):
            diff = target - nums[i]
            if diff in my_dict:
                my_list.append(i)
                my_list.append(my_dict[diff])
                break
            else:
                my_dict[nums[i]] = i

        return sorted(my_list)
        