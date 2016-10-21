import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        heap = []
        
        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)
            else:
                if num > heap[0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, num)
                    
        return heap[0]
