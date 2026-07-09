
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1 + nums2
        merged.sort()
        length = len(merged)
        
        if length % 2 == 0:
            return (merged[(length // 2) - 1] + merged[(length // 2)]) / 2.0
        else:
            return  merged[(length // 2)]
        

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        total = m + n
        half = (total + 1) // 2
        l, r = 0, m

        while l <= r:

            i = (l + r) // 2
            j = half - i

            nums1left = float("-inf") if i == 0 else nums1[i-1]
            nums1right = float("inf") if i == m else nums1[i]

            nums2left = float("-inf") if j == 0 else nums2[j-1]
            nums2right = float("inf") if j == n else nums2[j]

            if nums1left <= nums2right and nums2left <= nums1right:
                if total % 2 == 1:
                    return max(nums1left, nums2left)
                else:
                    return (max(nums1left, nums2left) + min(nums1right, nums2right)) / 2
            
            if nums1left > nums2right:
                r = i - 1
            else:
                l = i + 1