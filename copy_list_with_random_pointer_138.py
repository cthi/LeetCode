class Solution(object):

    def copyRandomList(self, head):
        ht = {}
        acc = None
        headRef = None

        while head:
            node = RandomListNode(head.label)
            node.random = head.random

            if not acc:
                headRef = node
            else:
                acc.next = node

            acc = node
            ht[head] = node
            head = head.next

        ref = headRef

        while ref:
            if ref.random:
                ref.random = ht[ref.random]
            ref = ref.next

        return headRef
