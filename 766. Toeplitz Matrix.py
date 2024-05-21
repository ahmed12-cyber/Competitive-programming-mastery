class Solution(object):
    def isToeplitzMatrix(self, matrix):
        M=len(matrix)
        N=len(matrix[0])
        
        for m in range(M-1,-1,-1):
            v=matrix[m][0]
            for x in range(0,M):
                if x+m < M and x < N :
                    
                    if v != matrix [x+m][x]:
                        return False
        
        for n in range(N-1,0,-1):
            v = matrix[0][n]
            for y in range(0,N):
                if y+n < N and y < M:
                    
                    if v != matrix[y][y+n]:
                        return False
        return True

