class MinStack:

    def __init__(self):
        # Initialize the main stack and the auxiliary stack to track minimums.
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        # Push the value onto the main stack.
        self.stack.append(val)
        
        # Update the minimum stack.
        if self.minStack:
            val = min(self.minStack[-1], val)
        self.minStack.append(val)

    def pop(self) -> None:
        # Remove the top element from both the main stack and the minimum stack.
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        # Return the top element of the main stack.
        return self.stack[-1]

    def getMin(self) -> int:
        # Return the top element of the minimum stack, which represents the minimum element in the main stack.
        return self.minStack[-1]