from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if i != j:
                    product = product * nums[j] 
            res.append(product)
        return res
    

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        prefix = [0] * length
        suffix = [0] * length
        res = [0] * length

        prefix[0] =  suffix[length-1] = 1
        for i in range(1, length):
            prefix[i] = nums[i-1] * prefix[i-1]
        for i in range(length - 2, -1, -1):
            suffix[i] = nums[i+1] * suffix[i+1]
        for i in range(length):
            res[i] = prefix[i] * suffix[i]
        return res
    

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i] 
        return res
