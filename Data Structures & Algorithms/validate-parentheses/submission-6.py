class Solution:
    def isValid(self, s: str) -> bool:
        if not s or len(s)%2==1:
            return False

        dic = {
            '(':')',
            '{': '}', 
            '[': ']'
        }
        temp = []
        for i in s:
            if i in dic:
                temp.append(i)
            else:
                if not temp: return False
                t = temp.pop()
                if dic[t]!=i:
                    return False
        
        if len(temp) > 0:
            return False
        else:    
            return True