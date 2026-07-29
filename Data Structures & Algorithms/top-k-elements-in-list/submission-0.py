class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        for i in nums:
            if i not in freqs:
                freqs[i] = 1
            else:
                freqs[i] += 1
        i = 0
        topFreqs = []
        while i < k:
            maxVal = max(freqs, key = freqs.get)
            topFreqs.append(maxVal)
            freqs.pop(maxVal)
            i += 1
        return topFreqs