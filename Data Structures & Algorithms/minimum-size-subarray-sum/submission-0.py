class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = 0
        running_sum = 0
        min_length = float("inf")

        for R in range(len(nums)):
            running_sum += nums[R]

            while running_sum >= target:
                min_length = min(min_length, R - L + 1)
                running_sum -= nums[L]
                L += 1

        return 0 if min_length == float("inf") else min_length




