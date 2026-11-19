from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
            array of nums
            return the top k most freq in any order

            create a frequency map num: freq

            I want to create a list of tuples that maps freq to nums

            create a new heap

            loop thru those freqs
                pop from when len heap > k
            
            return heap

        """

        frequencyMap = Counter(nums)

        frequencies = []

        for num, frequency in frequencyMap.items():
            frequencies.append((frequency, num))
        
        heap = []

        for freq in frequencies:
            heapq.heappush(heap, freq)

            if len(heap) > k:
                heapq.heappop(heap)
        
        return [num for frequency, num in heap]
