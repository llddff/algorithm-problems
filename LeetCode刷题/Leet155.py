class MinStack:
    def __init__(self):
        self.normal = []
        self.minval = []

    def push(self, node):
        self.normal.append(node)
        if not self.minval:
            self.minval.append(node)
        else:
            self.minval.append(min(node, self.minval[-1]))

    def pop(self):
        self.normal.pop()
        self.minval.pop()

    def top(self):
        return self.normal[-1]

    def getMin(self):
        return self.minval[-1]