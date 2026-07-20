class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currSum = 0

        minSum = nums[0]
        currSum2 = 0

        total_sum = 0

        for i in range(len(nums)):
            total_sum += nums[i]

            currSum = max(currSum, 0)
            currSum2 = min(currSum2, 0)

            currSum += nums[i]
            currSum2 += nums[i]

            maxSum = max(currSum, maxSum)
            minSum = min(currSum2, minSum)
        
        if maxSum < 0:
            return maxSum

        
        total_diff = total_sum - minSum
        if total_diff >= maxSum:
            return total_diff
        else:
            return maxSum

            