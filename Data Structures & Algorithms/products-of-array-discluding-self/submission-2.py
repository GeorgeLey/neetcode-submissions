class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Understand
            - Output: an array where for each value of nums it is the product of every single value in nums except that value
            - input: array of ints
            - Constraints: O(n) time and without using the division operation
            - Edge Case: len(nums) = 2, mix of neg and pos, all neg, all pos

        Match: Dynamic Programming
        Plan:
            - track a prefix and the result array
            - at first we want result array to hold the prefix product of that number at the beginning prefix will have a default value of 1. this will be done by going thru nums and multiplying the current value with the prefix value
            - Then I will track a postfix value with a default value of 1. loop thru the end of the result array and multiply each value of the postfix and then update the post fix by multiplying the val of nums at that position
            - Then I can return res
        
        Evaluate:
            - space complexity: O(1)??
            - time: O(n)
        """

        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res


        