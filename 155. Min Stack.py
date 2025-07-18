class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if not self.minstack or self.minstack[-1] >=val:
            self.minstack.append(val)
        
    def pop(self):
        """
        :rtype: None
        """
        if self.stack:
            val = self.stack.pop()
        if val == self.minstack[-1]:
            self.minstack.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]

        

    def getMin(self):
        """
        :rtype: int
        """
        if self.minstack:
            return self.minstack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()