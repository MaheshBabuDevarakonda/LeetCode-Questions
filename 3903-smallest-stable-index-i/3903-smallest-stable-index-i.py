class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        temp = 0
        ans = float('inf')
        n = len(nums)

        for i in range(n):
            temp = max(nums[0:i+1]) - min(nums[i:n])

            if temp <= k:
                ans = min(ans, i)

        if ans == float('inf'):
            return -1

        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna