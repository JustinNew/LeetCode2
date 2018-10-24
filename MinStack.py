# 155. Min Stack

# Google Tag

'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
'''

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.l = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if len(self.l) == 0:
            self.l.append((x, x))
        else:
            min = self.l[-1][1]
            if x < min:
                min = x
            self.l.append((x, min))
        return

    def pop(self):
        """
        :rtype: void
        """
        self.l.pop()
        return

    def top(self):
        """
        :rtype: int
        """
        return self.l[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        return self.l[-1][1]
