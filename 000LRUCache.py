# 146. LRU Cache

# Facebook Tag

'''
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
'''

class LRUCache:
    
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        from collections import deque
        
        self.n = capacity
        self.d = {}
        self.s = deque()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.d:
            self.s.remove(key)
            self.s.append(key)
            return self.d[key]
        else:
            return -1  

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.d:
            self.d[key] = value
            self.s.remove(key)
            self.s.append(key)
            return 
        else:
            if len(self.s) == self.n:
                t = self.s.popleft()
                self.d.pop(t)
            self.d[key] = value
            self.s.append(key)
            return

    ############################################################################################
    # O(1)
    # Use OrderedDict

    def __init__(self, capacity):
    	self.dic = collections.OrderedDict()
    	self.remain = capacity

    def get(self, key):
        if key not in self.dic:
            return -1
        v = self.dic.pop(key) 
        self.dic[key] = v   # set key as the newest one
        return v

    def set(self, key, value):
        if key in self.dic:    
            self.dic.pop(key)
        else:
            if self.remain > 0:
                self.remain -= 1  
            else:  # self.dic is full
                self.dic.popitem(last=False) 
        self.dic[key] = value
