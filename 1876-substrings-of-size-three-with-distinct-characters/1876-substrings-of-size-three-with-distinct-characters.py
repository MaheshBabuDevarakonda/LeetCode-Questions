class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count=0
        l=0
        temp=[]
        for r in range(len(s)):
            temp.append(s[r])
            if(r-l==3):
                temp.remove(s[l])
                l+=1
            if(r-l+1==3):
                if(len(set(temp))==3):
                    count+=1
        return count
            
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna