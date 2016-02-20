"""
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Notes:
-You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is
empty operations are valid.
-Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque
(double-ended queue), as long as you use only standard operations of a stack.
-You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).
"""

#=> Use two stacks. One stack to push elements and another to pop elements.

class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.popStack = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        #we will pop from popStack therefore if it is empty then dump all the data from stack into popStack
        if len(self.popStack)==0:
            n = len(self.stack)
            for i in range(n):
                x = self.stack.pop(-1)
                self.popStack.append(x)
        self.popStack.pop(-1)

    def peek(self):
        """
        :rtype: int
        """
        if len(self.popStack)==0:
            n = len(self.stack)
            for i in range(n):
                x = self.stack.pop(-1)
                self.popStack.append(x)
        return self.popStack[-1]


    def empty(self):
        """
        :rtype: bool
        """
        if (len(self.stack)+len(self.popStack))==0:
            return True
        return False

queue = Queue()
queue.push(2)
queue.push(3)
queue.push(5)
queue.push(1)
queue.push(8)
queue.pop()
queue.pop()
print queue.peek()