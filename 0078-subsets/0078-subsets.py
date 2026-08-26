class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def solve(ind, subset):
            if ind == len(nums):
                ans.append(subset.copy())
                return

            # Take nums[ind]
            subset.append(nums[ind])
            solve(ind + 1, subset)

            # Don't take nums[ind]
            subset.pop()
            solve(ind + 1, subset)

        solve(0, [])

        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna