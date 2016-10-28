class Solution(object):
    def reconstructQueue(self, people):
        people = sorted(people, key=lambda x: (-x[0], x[1]))
        q = []
        
        for p in people:
            q.insert(p[1], p)
            
        return q
