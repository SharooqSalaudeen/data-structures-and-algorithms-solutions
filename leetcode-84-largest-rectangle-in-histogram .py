from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        n= len(heights)
        for i in range(n):
            height = heights[i]
        
            rightMost = i+1
            while rightMost < n and heights[rightMost] >= height:
                rightMost += 1
            
            leftMost = i
            while leftMost >= 0 and heights[leftMost] >= height:
                leftMost -= 1

            rightMost -= 1
            leftMost += 1
            area = height * (rightMost - leftMost +1)
            maxArea = max(maxArea, area)
        return maxArea


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        for currIndex, currHeight in enumerate(heights):
            start = currIndex
            while stack and currHeight < stack[-1][1]:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (currIndex - index))
                start = index

            stack.append((start, currHeight))
        
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        
        return maxArea