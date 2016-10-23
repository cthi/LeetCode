class Solution(object):
    def findAnagrams(self, s, p):
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        p_hash = self.init_hash(p, primes)
        s_hash = self.init_hash(s[:len(p)], primes)
        
        indicies = []
        
        if p_hash == s_hash:
            indicies.append(0)
        
        for i in range(len(p), len(s)):
            s_hash /= primes[ord(s[i-len(p)]) - ord('a')]
            s_hash *= primes[ord(s[i]) - ord('a')]
            
            if p_hash == s_hash:
                indicies.append(i - len(p) + 1)
            
        return indicies
        
    def init_hash(self, s, primes):
        res = 1
        
        for char in s:
            res *= primes[ord(char) - ord('a')]
            
        return res

