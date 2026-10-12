class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # {7: 2}
        freqs = [[] for i in range(len(nums) + 1)] # [[],[],[7]]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        for num in list(count.keys()):
            freqs[count[num]].append(num)

        res = [] # [7]
        for i in range(len(freqs) - 1, 0, -1):
            for num in freqs[i]:
                res.append(num)
                if len(res) == k:
                    return res
                



        