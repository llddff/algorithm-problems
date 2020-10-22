class Solution:
    def __init__(self):
        self.stack1=[]
        self.stack2=[]
    def push(self, node):
        # write code here
        self.stack1.append(node)
    def pop(self):
        if self.stack2:
            return self.stack2.pop()
        elif not self.stack1:
            return
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()