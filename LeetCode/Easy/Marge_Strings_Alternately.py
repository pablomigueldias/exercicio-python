
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        resul = []
        i = 0
        while i < len(word1) or i < len(word2):
            if i < len(word1):
                resul.append(word1[i])
            if i < len(word2):
                resul.append(word2[i])
            i += 1
        return "".join(resul)

s = Solution()
print(s.mergeAlternately('abc','pqr'))
    



    

    

