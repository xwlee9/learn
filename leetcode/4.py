class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        l = len(nums1)
        d = l //2 
        if l % 2 == 0:    #偶数
            return ((nums1[d-1]+nums1[d])/2)
        else:
            return (float(nums1[d]))

