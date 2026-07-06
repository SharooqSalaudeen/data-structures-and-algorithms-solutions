class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {")":"(", "}": "{", "]": "["}
        stack = []
        for c in s:
            if c in mapping.values():
                stack.append(c)
            elif not stack or stack.pop() != mapping[c]:
                return False
        return not stack
