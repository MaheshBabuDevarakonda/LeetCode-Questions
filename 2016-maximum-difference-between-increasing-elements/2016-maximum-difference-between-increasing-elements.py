class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans = -1
        low=nums[0]

        for j in range(1, len(nums)):
            if low <nums[j]:
                temp=nums[j]-low
                ans=max(ans,temp)
            low=min(low,nums[j])

        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna