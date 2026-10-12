class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha = ''.join(char for char in s if char.isalnum())
        i = 0
        j = len(alpha) - 1

        while i < j:
            if alpha[i].lower() != alpha[j].lower():
                return False
            i += 1
            j -= 1
        return True