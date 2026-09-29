class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        ans=[]
        for i in range(len(matrix)):
            sum=0
            for j in range(len(matrix)):
                sum=sum+matrix[i][j]
            ans.append(sum)
        return ans