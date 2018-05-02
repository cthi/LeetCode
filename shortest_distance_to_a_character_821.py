class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        shortest = None
        output = [float('inf') for i in range(len(S))]
        
        for i, c in enumerate(S):
            if c == C:
                shortest = i
            if shortest is not None:
                output[i] = abs(i - shortest)
            
        shortest = None
        
        for i in range(len(S) - 1, -1 , -1):
            if S[i] == C:
                shortest = i
            if shortest is not None:
                output[i] = min(output[i], abs(shortest - i))

        return output
