class Solution:
    def sortColors(self, nums):
        i, j, k = -1, len(nums), 0
        while k < j:
            if nums[k] == 0:
                i += 1
                self.swap(nums, i, k)
                k += 1
            elif nums[k] == 2:
                j -= 1
                self.swap(nums, k, j)
            else:
                k += 1

    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]
