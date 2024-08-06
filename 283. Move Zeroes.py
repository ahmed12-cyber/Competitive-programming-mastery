class Solution:
    def moveZeroes(self, nums):
        i, n = -1, len(nums)
        for j in range(n):
            if nums[j] != 0:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
