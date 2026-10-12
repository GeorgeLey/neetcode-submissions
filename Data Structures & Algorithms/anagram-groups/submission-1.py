class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        annas = {}

        for word in strs:
            sortedWord = ''.join(sorted(word))
            if sortedWord not in annas:
                annas[sortedWord] = []
                annas[sortedWord].append(word)
            else:
                annas[sortedWord].append(word)
        return list(annas.values())