class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0

        max_count = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                count = 1
                j = i

                while j < (len(nums) - 1) and (nums[j+1] == 1):
                    j += 1
                    count += 1
                max_count = max(max_count, count)
        
        return max_count
