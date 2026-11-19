class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
            given numbers return [i, j] where i and j add up to the target answer with the smaller index 1st

            hashmap to store num: index
            loop thru the list
                check if target - curr in hashmap
                    return [min(curr, complement index), max(curr, complement index)]
        """

        comps = {}

        for i, val in enumerate(nums):
            if target - val in comps:
                return [min(i, comps[target - val]), max(i, comps[target - val])]
            else:
                comps[val] = i


        