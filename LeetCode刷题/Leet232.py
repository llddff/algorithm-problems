class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []

    def push(self, x):
        """
        Push element x to the back of queue.
        """
        if not self.s1:
            self.front = x
        self.s1.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()

    def peek(self):
        """
        Get the front element.
        """
        if self.s2:
            return self.s2[-1]
        return self.front

    def empty(self):
        return not (self.s1 or self.s2)
