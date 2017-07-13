class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        f1 = {e: i for i, e in enumerate(list1)}
        f2 = {e: i for i, e in enumerate(list2)}

        candidates = set(list1).intersection(set(list2))
        options = [(r, f1[r] + f2[r]) for r in candidates]

        smallest = min(options, key=lambda x: x[1])

        return [r[0] for r in options if r[1] == smallest[1]]
