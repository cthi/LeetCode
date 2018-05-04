class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        output = []
        
        for i, word in enumerate(S.split()):
            if word[0] not in 'aeiouAEIOU':
                word = word[1:] + word[0]
                
            word += 'ma' + 'a' * (i + 1)
            output.append(word)
            
        return " ".join(output)
