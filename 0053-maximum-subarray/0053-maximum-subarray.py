class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans=nums[0]
        sum=nums[0]
        for i in range(1,len(nums)):
            sum=max(nums[i],sum+nums[i])
            ans=max(sum,ans)
        return ans

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna