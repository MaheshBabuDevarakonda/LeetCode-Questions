class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans=float("-inf")
        sum=0
        for i in range(len(nums)):
            sum+=nums[i]
            ans=max(sum,ans)
            if sum<0:
                sum=0

        return ans

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna