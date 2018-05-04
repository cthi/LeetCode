from collections import defaultdict

class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        count = defaultdict(int)
        best_count = 0
        best_word = None
        
        for word in paragraph.split():
            word = word.lower()
            
            if word[-1] in '!?\',;.':
                word = word[:-1]
                
            if word not in banned:
                count[word] += 1
                if count[word] > best_count:
                    best_count = count[word]
                    best_word = word
                    
        return best_word
