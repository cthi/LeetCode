class Solution(object):

    def partition(self, head, x):
        headL = None
        headR = None
        left = None
        right = None

        while head:
            if head.val < x:
                if not headL:
                    headL = head

                if left:
                    left.next = head

                left = head
            else:
                if not headR:
                    headR = head

                if right:
                    right.next = head

                right = head

            head = head.next

        if right:
            right.next = None

        if not headL:
            return headR

        left.next = headR

        return headL
