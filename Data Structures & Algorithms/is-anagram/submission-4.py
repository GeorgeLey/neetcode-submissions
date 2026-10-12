class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {} 
        if len(s) != len(t): return False

        for i in range(len(s)):
        	if s[i] in s_dict:
        		s_dict[s[i]] += 1
        	else:
        		s_dict[s[i]] = 1
        	if t[i] in t_dict:
        		t_dict[t[i]] += 1
        	else:
        		t_dict[t[i]] = 1
        
        for char in s_dict:
            if char not in t_dict:
                return False
            if s_dict[char] != t_dict[char]:
                return False
        return True







