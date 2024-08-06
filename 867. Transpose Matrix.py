class Solution:
    def transpose(self, A):
        R, C = len(A), len(A[0])
        ans = [[0] * R for _ in range(C)]
        for r in range(R):
            for c in range(C):
                ans[c][r] = A[r][c]
        return ans
