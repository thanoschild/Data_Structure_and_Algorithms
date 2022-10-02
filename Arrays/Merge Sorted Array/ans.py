class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i, j, k = m - 1, n - 1, n + m - 1
        
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        
        while j>=0:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1
            
        