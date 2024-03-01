def merge(nums1, m, nums2, n):
    # Pointer for the last element in the original part of nums1
    i = m - 1  
    # Pointer for the last element in nums2
    j = n - 1  
    # Pointer for the last position in nums1
    k = m + n - 1  

    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            # Place the larger element at the end of nums1
            nums1[k] = nums1[i]  
            k -= 1
            i -= 1
        else:
            # Place the element from nums2 in nums1
            nums1[k] = nums2[j]  
            k -= 1
            j -= 1