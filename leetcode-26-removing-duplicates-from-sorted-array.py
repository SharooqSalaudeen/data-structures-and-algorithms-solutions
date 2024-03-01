from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1  # Initialize pointer l to 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:  # Check if current element is unique
                nums[l] = nums[r]  # Move unique element to position pointed by l
                l += 1  # Increment l

        return l  # Return count of unique elements