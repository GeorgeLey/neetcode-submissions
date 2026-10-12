class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # strs = ["act","pots","tops","cat","stop","hat"]
        
        my_dict = {} # {"act": ["act"], "opst": ["pots", "tops"], }

        for string in strs: # "act", "pots", "tops"
            if ("".join(sorted(string)) in my_dict):
                my_dict["".join(sorted(string))].append(string)
            else:
                my_dict["".join(sorted(string))] = [string]

        return list(my_dict.values())

# loop thru strs
# add them to a list with its anagrams


#    Add first word from list into List[List[str]]
#   Loop through array
# If List of list i i sorted == sorted(strs[i])
# Add to List of list i str[i]
# Else
# Create new list and add word to that list
# Add new list to list of lists
# [["hat"],["act", "cat"],["stop", "pots", "tops"], [“actor”]]
