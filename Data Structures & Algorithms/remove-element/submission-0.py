class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        # determine the size of nums
        nums_length = len(nums)

        # iterate through the array of nums and keep count of
        # the number of elements that are not equal to val

        result = []
        count = 0
        for i in range(nums_length):
            if nums[i] != val:
                count += 1
                result.append(nums[i])
        
        nums[:count] = result
        return count

            
        