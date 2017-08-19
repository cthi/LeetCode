# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def ll_len(head):
            count = 0

            while head:
                count += 1
                head = head.next

            return count

        def ll_merge(a, b):
            head = None
            postHead = None

            while a and b:
                if a.val < b.val:
                    if not head:
                        head = a
                        postHead = a
                    else:
                        head.next = a
                        head = head.next
                    a = a.next
                else:
                    if not head:
                        head = b
                        postHead = b
                    else:
                        head.next = b
                        head = head.next
                    b = b.next

            while a:
                head.next = a
                head = head.next
                a = a.next

            while b:
                head.next = b
                head = head.next
                b = b.next

            return postHead

        def getN(head, N):
            count = 0
            prev = None

            while count != N:
                count += 1
                prev = head
                head = head.next

            if prev:
                prev.next = None
            return head

        def mergeSort(head):
            length = ll_len(head)

            if length == 1:
                return head

            first = head
            rest = getN(head, length // 2)

            return ll_merge(mergeSort(first), mergeSort(rest))

        if not head:
            return head

        return mergeSort(head)
