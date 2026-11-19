from collections import deque

class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    """
        hashmap to quickly look up if a key is in the cache
        1 - 2 - 1

        constructor:
            - store capacity
            - double linked list where the left most node is the LRU and the right is the MRU
            - hashmap initialized here, <- this hash map is going to store the nodes of the linked list as the value so that i dont have to search the list I can just look up its pointers and reattach them
        
        get:
            - if key else -1
            - move it to the front of the list
        
        put:
            - if the key exists update its value and move it to the front linked
            - else just add it to the front linked and add to the hashmap
            - if capacity is exceed, remove lru
    """

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.left, self.right = Node(0, 0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
        
