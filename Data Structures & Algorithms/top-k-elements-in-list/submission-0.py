class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}

        for num in nums:
            if num not in freqs:
                freqs[num] = 1
            else:
                freqs[num] += 1
        
        result = []
        for i in range(k):
            largestVal = 0
            largestKeyVal = 0
            for key in list(freqs.keys()):
                if freqs[key] > largestVal:
                    largestVal = freqs[key]
                    largestKeyVal = key
            result.append(largestKeyVal)
            del freqs[largestKeyVal]

        return result

        