class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if s=="":
            return 0
        
        ans=1

        l=0
        r=1
        temp=s[0]
        while r<len(s):
            
            if s[r] not in temp:
                temp+=s[r]
                r+=1
                ans=max(ans,len(temp))
            else:
                l+=1
                temp = temp[1:]
            
        return ans