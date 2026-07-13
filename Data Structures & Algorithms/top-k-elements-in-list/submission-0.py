class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequency_map = {}
        result = []
        for num in nums:
            if num not in frequency_map:
                frequency_map[num] = 1
            else:
                frequency_map[num] += 1
        
        buckets = [[] for i in range(len(nums) + 1)]
        for key, freq in frequency_map.items():
            buckets[freq].append(key)

        for freq in range(len(buckets) - 1, 0, -1):
            for key in buckets[freq]:
                result.append(key)
                if len(result) == k:
                    return result

        return result