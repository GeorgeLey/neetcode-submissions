class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} #
        freqs = [[] for i in range(len(nums) + 1)] # [], [], [], [], [], [], []

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        for key, val in count.items():
            freqs[val].append(key)
        
        res = []
        for i in range(len(freqs) - 1, -1, -1):
            if len(res) >= k:
                break
            for j in range(len(freqs[i])):
                if len(res) <= k:
                    res.append(freqs[i][j])
                else:
                    break
        return res