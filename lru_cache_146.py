class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.ht = {}
        self.q = []

    def get(self, key):
        """
        :rtype: int
        """
        if key in self.ht:
            self.q.remove(key)
            self.q.append(key)

            return self.ht[key]
        else:
            return -1

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.ht:
            self.ht[key] = value
            self.q.remove(key)
            self.q.append(key)
        else:
            if len(self.q) == self.capacity:
                rem = self.q.pop(0)
                del self.ht[rem]

            self.q.append(key)
            self.ht[key] = value
