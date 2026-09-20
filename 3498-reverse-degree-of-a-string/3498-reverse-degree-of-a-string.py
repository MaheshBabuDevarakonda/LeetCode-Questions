class Solution:
    def reverseDegree(self, s: str) -> int:
        dici = {}
        sum=0
        for i in range(26):
            dici[chr(ord('a') + i)] = 26 - i
        k=1
        for i in range(len(s)):
            sum+=(dici[s[i]]*k)
            k+=1
        return sum        


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna