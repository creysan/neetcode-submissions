class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(n^2) runtime
        # Auxilliary space: O(n)
        # Total space: O(n)
        freqs = {}
        for i in nums:
            # O(n) runtime
            if i not in freqs:
                freqs[i] = 1
            else:
                freqs[i] += 1
        i = 0
        topFreqs = []
        while i < k:
            # O(n + mk)
            maxVal = max(freqs, key = freqs.get)
            topFreqs.append(maxVal)
            freqs.pop(maxVal)
            i += 1
        return topFreqs