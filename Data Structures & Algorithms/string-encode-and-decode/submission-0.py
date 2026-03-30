class Solution:

    def encode(self, strs: List[str]) -> str:

        ens = ""
        for s in strs:
            ens+= str(len(s))+"#"+s
        return ens

    def decode(self, s: str) -> List[str]:

        des = []
        i = 0
        while i<len(s):

            j=i
            while(s[j]!='#'):
                j+=1
            
            length = int(s[i:j])
            start = j+1
            end = start+length
            des.append(s[start:end])

            i=end
        
        return des