from heapq import heappush, heappop

class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if not nums1 or not nums2:
            return []
        pairs = []
        heap = [(nums1[0] + nums2[0], 0, 0)]
        seen = set()

        while len(pairs) != k and heap:
            _, i, j = heappop(heap)
            pairs.append((nums1[i], nums2[j]))

            if (i + 1, j) not in seen and i + 1 < len(nums1) and j < len(nums2):
                seen.add((i + 1, j))
                heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))
            if (i, j + 1) not in seen and i < len(nums1) and j + 1 < len(nums2):
                seen.add((i, j + 1))
                heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))

        return pairs
