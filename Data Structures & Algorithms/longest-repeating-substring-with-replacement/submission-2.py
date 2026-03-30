class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        count = {}
        ans = 0
        max_freq = 0

        left=0
        for i in range(len(s)):
            
            if s[i] in count:
                count[s[i]]+=1
            else:
                count[s[i]]=1
            
            max_freq = max(max_freq, count[s[i]])

            if (i-left+1)-max_freq>k:
                count[s[left]]-=1
                left+=1
            
            ans=max(ans,i-left+1)
        
        return ans