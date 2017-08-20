from string import ascii_lowercase


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        def bfs(beginWord, endWord, wordSet):
            if endWord not in wordSet:
                return 0

            X = set([beginWord])
            Y = set([endWord])
            N = len(beginWord)
            length = 1

            while X:
                length += 1
                Xn = set()

                for curWord in X:
                    wordSet.discard(curWord)

                    for i in range(N):
                        for char in ascii_lowercase:
                            nextWordMaybe = curWord[:i] + \
                                char + curWord[i + 1:]
                            if nextWordMaybe in Y:
                                return length
                            elif nextWordMaybe in wordSet:
                                Xn.add(nextWordMaybe)

                X = Xn

                if len(X) > len(Y):
                    X, Y = Y, X
            return 0

        return bfs(beginWord, endWord, set(wordList))
