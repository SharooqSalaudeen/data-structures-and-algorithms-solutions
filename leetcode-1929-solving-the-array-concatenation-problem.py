from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # Calculate the length of the input array
        n = len(nums)
        
        # Initialize an empty array to store the concatenated array
        ans = []
        
        # Iterate over indices of the new array
        for i in range(2 * n):
            # Assign values to the new array
            ans.append(nums[i % n])  # Cycling through the elements of nums
            
        # Return the concatenated array
        return ans

# Example usage:
# nums = [1, 2, 3]
# solution = Solution()
# concatenated_array = solution.getConcatenation(nums)
# print(concatenated_array)