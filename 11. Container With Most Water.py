class Solution:
    def maxArea(self, height):
        i, j = 0, len(height) - 1
        ans = 0
        while i < j:
            t = min(height[i], height[j]) * (j - i)
            ans = max(ans, t)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return ans
