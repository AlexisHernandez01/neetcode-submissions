class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        window = list()
        L = 0
        totalSum = 0
        count = 0

        for R in range(len(arr)):
            totalSum += arr[R]
            if R - L + 1 == k:
                if totalSum >= threshold * k:
                    count += 1
                    print(window)
                totalSum -= arr[L]
                L += 1           
        return count