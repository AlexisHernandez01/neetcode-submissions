class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        one, two = 0, 0
        while two < n:
            if one >= m + two or nums2[two] <= nums1[one]:
                nums1[one + 1 :m + two + 1] = nums1[one:m + two]
                print("After shifting nums1: ", nums1)
                print(nums2[two])
                nums1[one] = nums2[two]
                print("After placing nums2[two] in nums1: ", nums1)
                two += 1
            else:
                one += 1