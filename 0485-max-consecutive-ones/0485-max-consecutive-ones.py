class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # Current Complexity: Time O(n), Space O(1). This is optimal.
        # Logic Issue: You are incrementing 'count' regardless of whether nums[r] is 1 or 0.
        # Also, you are not updating 'ans' to track the maximum count found so far.
        ans=0
        count=0
        l=0
        for r in range(len(nums)):
            if nums[r]==0:
                count=0
            # Hint 1: Only increment count if nums[r] is 1.
            # Hint 2: After updating count, use ans = max(ans, count) to store the peak.
            if nums[r] == 1:
                count += 1
            ans = max(count, ans)
        # Hint 3: You should return 'ans' instead of the final 'count'.
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna