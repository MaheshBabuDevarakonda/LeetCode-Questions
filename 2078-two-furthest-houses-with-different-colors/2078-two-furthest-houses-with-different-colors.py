class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        gmax=0
        for i in range(len(colors)):
            for j in range(len(colors)):
                if colors[i]!=colors[j]:
                    lmax=(abs(i-j))
            gmax=max(gmax,lmax)
        return gmax
                    
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna