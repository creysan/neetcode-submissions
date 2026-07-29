class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        topK = []
        for i in nums:
            # O(n) runtime
            if i not in freqs:
                freqs[i] = 1
            else:
                freqs[i] += 1
    
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, frequency in freqs.items():
            buckets[frequency].append(num)
    
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                topK.append(num)
                if len(topK) == k:
                    return topK
