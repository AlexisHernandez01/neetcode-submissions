class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        num_set = set(nums)
        
        max_count = 1

        for num in nums:
            if (num - 1) not in nums:
                current_num = num
                count = 1
                
                while (current_num + 1) in nums:
                    current_num += 1
                    count += 1
                
                max_count = max(max_count, count)
        return max_count