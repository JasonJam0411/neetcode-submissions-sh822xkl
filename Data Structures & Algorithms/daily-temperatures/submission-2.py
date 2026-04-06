class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0]*n
        temp = []
        for i in range(n):
            
            while temp and temperatures[i] > temperatures[temp[-1]]:
                pre_index = temp.pop()
                ans[pre_index] = i-pre_index
            
            temp.append(i)

        return ans