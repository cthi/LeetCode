class Solution(object):

    def addTwoNumbers(self, l1, l2):
        res = self.asInt(l1) + self.asInt(l2)

        ans = None
        head = None

        for char in str(res):
            node = ListNode(int(char))

            if ans:
                ans.next = node
            else:
                head = node

            ans = node

        return head

    def asInt(self, node):
        num = ""

        while node:
            num += str(node.val)
            node = node.next

        return int(num)
