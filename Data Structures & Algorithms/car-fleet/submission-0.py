class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = sorted(zip(position,speed), reverse=True)

        current_time = 0
        ans = 0

        for p,s in cars:
            time = (target-p)/s

            if time>current_time:
                current_time=time
                ans+=1
        
        return ans
