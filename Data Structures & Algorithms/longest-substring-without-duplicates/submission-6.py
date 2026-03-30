class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        record = {}
        left=0
        ans=0

        for i in range(len(s)):

            if s[i] in record and record[s[i]]>=left:
                left = record[s[i]]+1
            
            record[s[i]] = i
            ans = max(ans, i-left+1)
        
        return ans