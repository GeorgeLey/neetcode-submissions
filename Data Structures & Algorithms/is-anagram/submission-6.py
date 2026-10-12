class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Time O(n)
        # Space O(n)
        sSorted = sorted(s)
        tSorted = sorted(t)

        if sSorted == tSorted:
            return True
        return False
