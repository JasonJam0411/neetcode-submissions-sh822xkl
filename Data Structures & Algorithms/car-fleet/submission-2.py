class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 1. 將 position 和 speed 兩兩綁定，並依照「位置」從大到小排序（由近到遠）
        # zip(position, speed) 會變成類似 [(10, 2), (8, 4), (0, 1)] 的結構
        # reverse=True 代表從大到小排
        cars = sorted(zip(position, speed), reverse=True)
        
        ans = 0              # 記錄總共有幾個車隊
        current_slowest = 0  # 記錄目前擋在前面的車隊「抵達所需的時間」
        
        # 2. 從最靠近終點的車開始，一台一台往後看
        for p, s in cars:
            # 計算這台車單獨開，需要多少時間
            time = (target - p) / s
            
            # 3. 判斷會不會追撞
            # 如果這台車需要的時間「大於」前面的車隊，代表它比較慢，追不上前車！
            # 既然追不上，它就會自己帶頭形成一個「新的車隊」
            if time > current_slowest:
                ans += 1
                current_slowest = time  # 更新這組新車隊的時間，讓後面的車來比較
            
            # (如果 time <= current_slowest，代表它會追上前車併入車隊，ans 就不用加 1，什麼都不用做)
                
        return ans
