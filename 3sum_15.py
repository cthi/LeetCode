class Solution(object):
    def threeSum(self, nums):
        negatives = {}
        positives = {}
        numZeros = 0
        ans = []
        
        for num in nums:
            if num < 0:
                if num in negatives:
                    negatives[num] += 1
                else:
                    negatives[num] = 1
            elif num > 0:
                if num in positives:
                    positives[num] += 1
                else:
                    positives[num] = 1
            else:
                numZeros += 1
                
        if numZeros >= 3:
            ans.append([0, 0, 0])
            
        for neg in negatives:
            once = False
            used = set()
            for pos in positives:
                maybeVal = abs(neg) - pos
                
                if maybeVal in used:
                    continue
                
                used.add(maybeVal)
                used.add(pos)
                
                if maybeVal in positives and (maybeVal != pos or positives[maybeVal] >= 2):
                    ans.append([neg, pos, maybeVal])
                        
                if not once and numZeros > 0 and abs(neg) in positives:
                    ans.append([neg, abs(neg), 0])
                    once = True
        
        for pos in positives:
            used = set()
            
            for neg in negatives:
                maybeVal = -(pos + neg)
                
                if maybeVal in used:
                    continue
                
                used.add(maybeVal)
                used.add(neg)
                
                if maybeVal in negatives and (maybeVal != neg or negatives[maybeVal] >= 2):
                    ans.append([pos, neg, maybeVal])
                    
        return ans
        
