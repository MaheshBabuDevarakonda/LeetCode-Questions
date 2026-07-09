class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans=0
        minv=prices[0]
        for i in range(1,len(prices)):
            ans=max(ans,prices[i]-minv)
            minv=min(minv,prices[i])
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna