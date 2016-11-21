class Solution(object):

    def detectCycle(self, head):
        seen = set()

        while head:
            if head in seen:
                return head
            else:
                seen.add(head)

            head = head.next

        return None
