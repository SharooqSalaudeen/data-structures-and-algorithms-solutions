from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # Initialize an empty record
        arr = []

        # Iterate through operations
        for i in range(len(operations)):
            # Check each operation
            match operations[i]:
                case "+":
                    arr.append(arr[-1] + arr[-2])  # Record sum of last two scores
                case "D":
                    arr.append(2 * arr[-1])  # Record double of last score
                case "C":
                    arr.pop()  # Remove last score
                case _:
                    arr.append(int(operations[i]))  # Record the score directly
        
        # Calculate the sum of all scores
        total_sum = sum(arr)
        
        # Return the sum
        return total_sum