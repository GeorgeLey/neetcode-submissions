class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)): # 0
            for j in range(len(nums)): # 1
                if i != j and nums[i] + nums[j] == target:
                    if j < i:
                        return [j,i]
                    else:
                        return [i,j]