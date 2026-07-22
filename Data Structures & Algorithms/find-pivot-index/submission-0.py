class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        totalSum = 0
        prefix = []

        for num in nums:
            totalSum += num
            prefix.append(totalSum)

        for i in range(len(nums)):
            if prefix[i] - nums[i] == totalSum - prefix[i]:
                return i
        return -1

