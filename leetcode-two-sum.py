class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
    

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = []

        for i, num in enumerate(nums):
            A.append([num, i])
        
        A.sort()

        i, j = 0, len(nums)-1
        while i < j:
            curr = A[i][0] + A[j][0]
            if curr == target:
                return [min(A[i][1], A[j][1]), max(A[i][1], A[j][1])]
            elif target > curr:
                i += 1
            else:
                j -= 1

        return []
    

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i