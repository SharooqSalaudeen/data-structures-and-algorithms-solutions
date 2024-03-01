class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0  # Initialize a pointer for the left boundary of the window
        for r in range(len(nums)):  # Iterate through the array using a pointer for the right boundary
            if nums[r] != val:  # If the current element is not equal to val
                nums[l] = nums[r]  # Move the current element to the left boundary
                l += 1  # Increment the left boundary pointer
        return l  # Return the count of elements not equal to val