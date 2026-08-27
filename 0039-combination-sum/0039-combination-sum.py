class Solution:
    def combinationSum(self, candidates, target):
        ans = []

        def solve(ind, target, ds):

            # Target reached
            if target == 0:
                ans.append(ds.copy())
                return

            # No candidates left
            if ind == len(candidates):
                return

            # Take candidates[ind]
            if candidates[ind] <= target:
                ds.append(candidates[ind])

                # Same index because we can reuse the element
                solve(ind, target - candidates[ind], ds)

                # Backtrack
                ds.pop()

            # Don't take candidates[ind]
            solve(ind + 1, target, ds)

        solve(0, target, [])

        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna