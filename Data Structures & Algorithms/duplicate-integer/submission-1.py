class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_set = set() #1,2,3
        if (len(nums) == 0):
            return False
        for num in nums: #on: 1,2,3,3
            if num in num_set: #if 1 in num_set? No, is 2 in num_set? No, is 3 in num_set? No, is 3 in num_set? yuh
                return True
            num_set.add(num) #add 1, add 2
        return False