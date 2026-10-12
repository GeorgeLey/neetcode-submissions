class Solution:
    def findMin(self, nums: List[int]) -> int:

        count = 1
        index = 0
        while(count < len(nums)):
            if (nums[index] < nums[index + 1]):
                count += 1
                index += 1
            else:
                break
        if (count == len(nums)):
            return nums[0]
        else:
            return nums[count]

