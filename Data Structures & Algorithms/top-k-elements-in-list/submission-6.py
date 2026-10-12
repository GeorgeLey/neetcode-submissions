class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        import heapq
        freqs = Counter(nums)

        freqHeap = []

        for key, v in freqs.items():
            heapq.heappush(freqHeap, (-v, key))
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(freqHeap)[1])
        
        return res