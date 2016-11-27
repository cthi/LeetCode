class Solution(object):

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        return self._wordBreak(s, wordDict, {})

    def _wordBreak(self, s, wordDict, memo):
        if s in memo:
            return memo[s]
        if not s:
            return [""]
        else:
            combinations = []

            for i in range(1, len(s) + 1):
                word = s[:i]
                if word in wordDict:
                    for ans in self._wordBreak(s[i:], wordDict, memo):
                        if ans:
                            combinations.append(word + " " + ans)
                        else:
                            combinations.append(word)

            memo[s] = combinations
            return combinations
