class Solution:
    def isValid(self, s: str) -> bool:
        # Initialize an empty stack to keep track of opening brackets
        stack = []
        # Create a mapping dictionary to map closing brackets to their corresponding opening brackets
        mapping = {")": "(", "]": "[", "}": "{"}

        # Iterate through each character in the input string
        for char in s:
            # If the stack is not empty and the current character is a closing bracket,
            # and the top of the stack contains the corresponding opening bracket,
            # pop the element from the stack as they form a valid pair
            if stack and char in mapping and stack[-1] == mapping[char]:
                stack.pop()
            # Otherwise, if the character is not a closing bracket or if it doesn't match
            # the corresponding opening bracket at the top of the stack, push it onto the stack
            else:
                stack.append(char)
        
        # After processing all characters in the string, check if the stack is empty
        # If it is, return True indicating that the input string is valid; otherwise, return False
        return len(stack) == 0