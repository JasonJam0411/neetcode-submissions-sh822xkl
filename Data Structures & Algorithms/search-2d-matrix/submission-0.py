class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        n = len(matrix)
        m = len(matrix[0])
        
        left=0
        right=n*m-1
        
        while left<=right:
            mid = (left+right) //2

            mid_val = matrix[mid//m][mid%m]

            if mid_val == target:
                return True
            elif mid_val < target:
                left+=1
            else:
                right-=1
        
        return False