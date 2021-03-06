import heapq
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        head = None
        node = None

        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, node))

        while heap:
            (val, nextNode) = heapq.heappop(heap)

            if nextNode.next:
                heapq.heappush(heap, (nextNode.next.val, nextNode.next))

            if not head:
                head = nextNode
            else:
                node.next = nextNode
            node = nextNode

        return head
