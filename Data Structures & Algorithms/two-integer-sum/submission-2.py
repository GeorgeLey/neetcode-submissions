class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = {}
        
        for i in range(len(nums)):
            sums[nums[i]] = i
        
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in sums:
                if sums[comp] != i:
                    if sums[comp] < i:
                        return [sums[comp], i]
                    else:
                        return [i, sums[comp]]
                