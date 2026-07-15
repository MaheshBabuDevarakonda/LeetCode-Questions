class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        k=set()
        count=0
        for i in range(len(s)-2):
            k.clear()
            for j in range(i,i+3):
                k.add(s[j])
            if len(k)==3:
                count+=1
        return count
            
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna