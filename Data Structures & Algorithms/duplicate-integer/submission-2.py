class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        noDups = set(nums)

        if len(noDups) < len(nums):
            return True
        return False
        