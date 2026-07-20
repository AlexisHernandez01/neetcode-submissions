class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        my_set = set()
        L = 0

        for R in range(len(nums)):

            if R - L > k:
                my_set.remove(nums[L])
                L += 1
            
            if nums[R] in my_set:
                return True
            my_set.add(nums[R])

        return False