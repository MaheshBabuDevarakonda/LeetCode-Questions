class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count=0
        dici={}
        for i in stones:
            dici[i]=stones.count(i)
        for i in jewels:
            if i in dici:
                count=count+dici[i]
        return count
        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna