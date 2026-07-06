from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        mArea = 0
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                area = min(heights[i], heights[j]) * (j-i)
                mArea = max(area, mArea)
        return mArea

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights) -1
        maxArea = 0
        while l<r:
            currentArea = min(heights[l], heights[r]) * (r-l)
            maxArea = max(maxArea, currentArea)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxArea
        