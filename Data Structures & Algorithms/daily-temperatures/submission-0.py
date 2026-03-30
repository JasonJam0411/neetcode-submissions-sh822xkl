class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0]*n
        temp = []

        for i in range(n):

            while temp and temperatures[i] > temperatures[temp[-1]]:
                prev = temp.pop()
                ans[prev] = i - prev


            temp.append(i)
        
        return ans