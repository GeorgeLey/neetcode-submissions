class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        sChars = {}
        tChars = {}
        
        for let in s:
            if let in sChars:
                sChars[let] += 1
            else:
                sChars[let] = 1
        for let in t:
            if let in tChars:
                tChars[let] += 1
            else:
                tChars[let] = 1
        
        for key in sChars.keys():
            if key in tChars:
                if sChars[key] != tChars[key]:
                    return False
            else:
                return False

        if len(s) != len(t):
            return False

        return True
