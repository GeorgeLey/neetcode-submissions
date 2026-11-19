class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
            numbers in increasing order and I need to find the target value

            two pointer solution because of the sort

            l = 0
            r = end of list

            while l < r
                if left + right == target return [l,r]
                if left + right is > than target decrement r
                else increment l
            
            Time O(n)
            Space O(1)
        """


        l = 0
        r = len(numbers) - 1

        while l < r:
            guess = numbers[l] + numbers[r]
            if guess == target:
                return [l + 1, r + 1]
            elif guess > target:
                r -= 1
            else:
                l += 1