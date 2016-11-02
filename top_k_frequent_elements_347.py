from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        occurences = Counter()
        
        for n in nums:
            occurences[n] += 1
            
        return [count[0] for count in occurences.most_common()[:k]]
        
