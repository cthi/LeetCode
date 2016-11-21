import heapq


class Solution(object):

    def thirdMax(self, nums):
        heap = []
        seen = set()

        for num in nums:
            if num in seen:
                continue
            else:
                seen.add(num)

            if len(heap) < 3:
                heapq.heappush(heap, num)
            else:
                if num > heap[0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, num)

        if len(heap) == 3:
            return heap[0]
        else:
            return max(heap)
