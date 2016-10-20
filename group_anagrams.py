from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        anagrams = defaultdict(list)
        
        for s in strs:
            sortedStr = ''.join(sorted(s))
            anagrams[sortedStr].append(s)
        
        return anagrams.values()
