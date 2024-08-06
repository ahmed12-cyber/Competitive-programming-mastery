class Solution:
    def maxOperations(self, nums, k):
        nums.sort()
        l, r = 0, len(nums) - 1
        ans = 0
        while l < r:
            s = nums[l] + nums[r]
            if s == k:
                ans += 1
                l += 1
                r -= 1
            elif s > k:
                r -= 1
            else:
                l += 1
        return ans
