class Solution:

    def encode(self, strs: List[str]) -> str:
        #  s = 5#World
        result = ""
        for word in strs:
            result += str(len(word)) + "#" + word
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        index = 0
        while(index < len(s)):
            try:
                word_len = int(s[index:(s.index("#"))])
            except ValueError:
                break
            if word_len == 0:
                result.append("")
                try:
                    s = s[2 + word_len:]
                except Exception as e:
                    break
            else: # 2 
                result.append(s[(index + len(str(word_len)) + 1):(index + len(str(word_len)) + 1 + word_len)])
                s = s[len(str(word_len)) + word_len + 1:]
            index = 0
        
        return result
