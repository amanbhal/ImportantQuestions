"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

"""

#=> aim is to perform get and set operations in O(1).
#=> to perform get operation in O(1) we make use of hashMap which stores keys and nodes of doubly linked list as
#   values.
#=> to perform set operation in O(1) we make use of douly linked list. Each node stores key and value. the most
#   recently used element is at head and the least used element is at end.
#=> whenever a key is used in either get or set its corresponding node is first removed from its current position
#   and added to the starting of the doubly linked list.
#=> when new key value pair is to be inserted and the capacity of the hashMap is full we remove the end node from
#   the doubly linked list and add the new node at the starting of the list.

class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        #initialize the hashMap and capacity and the doubly linked list head and end.
        self.hashMap = {}
        self.capacity = capacity
        self.head = None
        self.end = None

    def get(self, key):
        """
        :rtype: int
        """
        try:
            temp = self.hashMap[key]
        except KeyError:
            return -1
        self.remove(temp)
        self.makeHead(temp)
        return temp.value

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        temp = Node(key,value)
        if key in self.hashMap:
            self.remove(self.hashMap[key])
            self.makeHead(temp)
            self.hashMap[key] = temp
        else:
            #if Cache is at the full capacity
            if len(self.hashMap)>=self.capacity:
                del self.hashMap[self.end.key]
                self.remove(self.end)
                self.makeHead(temp)
                self.hashMap[key] = temp
            else:
                self.makeHead(temp)
                self.hashMap[key] = temp

    def remove(self,node):
        if node==self.end:
            #if end node is the only node
            if self.end.left==None:
                self.end = None
                self.head = None
            else:
                self.end.left.right = None
                temp = self.end.left
                self.end.left = None
                self.end = temp
        else:
            #if the node to be deleted is the head
            if node==self.head:
                node.right.left = None
                self.head = node.right
                node.right = None
            else:
                node.left.right = node.right
                node.right.left = node.left
                node.right = None
                node.left = None

    def makeHead(self,node):
        if self.head==None:
            self.head = node
            self.end = node
        else:
            node.right = self.head
            self.head.left = node
            self.head = node