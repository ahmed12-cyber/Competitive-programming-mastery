class Solution:
    def smallerNumbersThanCurrent(self, nums):
        arr = sorted(nums)
        result = []
        for num in nums:
            result.append(self.search(arr, num))
        return result

    def search(self, nums, x):
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) // 2
            if nums[mid] >= x:
                r = mid
            else:
                l = mid + 1
        return l
