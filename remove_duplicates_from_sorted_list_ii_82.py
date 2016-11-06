class Solution(object):
    def deleteDuplicates(self, head):
        ht = {}
        it = head
        
        while head:
            if head.val in ht:
                ht[head.val] += 1
            else:
                ht[head.val] = 1
                
            head = head.next
            
        headRef = None
        last = None
        
        while it:
            if ht[it.val] > 1:
                if last:
                    last.next = it.next
                    it = it.next
                else:
                    it = it.next
            else:
                if not last:
                    headRef = it
                    
                last = it
                it = it.next
                
        return headRef
                    
