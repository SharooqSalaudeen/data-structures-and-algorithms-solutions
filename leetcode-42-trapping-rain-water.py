from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)
        res = 0

        for i in range(n):
            leftMax = rightMax = height[i]

            for j in range(i):
                leftMax = max(leftMax, height[j])
            for j in range(i+1, n):
                rightMax = max(rightMax, height[j])
            res += min(leftMax, rightMax) - height[i]

        return res
    

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        n = len(height)
        res = 0 
        prefix = [0] * n
        suffix = [0] * n

        prefix[0] = height[0]
        for i in range(1, n):
            prefix[i] = max(prefix[i-1], height[i])
        
        suffix[n-1] = height[n-1]
        for j in range(n-2, -1, -1):
            suffix[j] = max(suffix[j+1], height[j])
        
        for i in range(n):
            res += min(prefix[i], suffix[i]) - height[i]

        return res
        

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        res = 0
        l, r = 0 , len(height) -1 
        leftMax, rightMax = height[l], height[r]
        while l<r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
            
        return res
