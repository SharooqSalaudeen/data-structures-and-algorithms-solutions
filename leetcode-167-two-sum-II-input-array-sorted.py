from typing import List 

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range (len(numbers)):
            for j in range (i+1, len(numbers)):
                if (numbers[i] + numbers[j] == target):
                    return [i+1, j+1]

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l<r:
            current = numbers[l] + numbers[r]
            if current < target:
                l += 1
            if current > target:
                r -= 1
            if current == target:
                return [l+1, r+1]