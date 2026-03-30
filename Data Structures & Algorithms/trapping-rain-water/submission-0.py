class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)
        left = [0]*n
        right = [0]*n

        left_max=0
        right_max=0
        
        for i in range(n):
            
            if height[i]>left_max:
                left_max = height[i]
            
            left[i] = left_max
        
        for i in range(n-1,-1,-1):
            i
            if height[i]>right_max:
                right_max = height[i]
            
            right[i] = right_max
        
        ans=0
        
        for i in range(n):
            water = min(left[i],right[i]) - height[i]
            if water>0:
                ans+=water
        return ans