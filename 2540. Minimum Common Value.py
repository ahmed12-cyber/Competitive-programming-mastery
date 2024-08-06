class Solution(object):
    def getCommon(self, nums1, nums2):
        m, n = len(nums1), len(nums2)
        i, j = 0, 0
        while i < m and j < n:
            if nums1[i] == nums2[j]:
                return nums1[i]
            if nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return -1
