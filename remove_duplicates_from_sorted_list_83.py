class Solution(object):
    def deleteDuplicates(self, head):
        last = None
        headRef = head
        
        while head:
            if not last:
                last = head
            else:
                if last.val == head.val:
                    last.next = head.next
                else:
                    last = head
                    
            head = head.next
                    
        return headRef
        
