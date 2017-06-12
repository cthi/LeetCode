from collections import defaultdict


class Solution:
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        dups = defaultdict(list)

        for p in paths:
            z = p.split()
            path = z[0]
            files = z[1:]

            for f in files:
                contents = f[f.find("(") + 1:f.find(")")]
                fullpath = path + "/" + f[:f.find("(")]
                dups[contents].append(fullpath)

        return [v for k, v in dups.items() if len(v) > 1]
