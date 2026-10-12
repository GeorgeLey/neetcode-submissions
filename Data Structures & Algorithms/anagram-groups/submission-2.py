class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        annas = defaultdict(list)

        for word in strs:
            frequencies = [0] * 26
            for letter in word:
                frequencies[ord(letter) - ord('a')] += 1
            annas[tuple(frequencies)].append(word)
        return list(annas.values())