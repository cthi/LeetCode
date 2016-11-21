from collections import Counter


class Solution(object):

    def frequencySort(self, s):
        occurences = Counter()

        for char in s:
            occurences[char] += 1

        ans = ""

        for count in occurences.most_common():
            ans += count[0] * count[1]

        return ans
