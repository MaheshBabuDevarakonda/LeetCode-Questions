class Solution:
    def tribonacci(self, n: int) -> int:
        # Issue: dp list size is n+1, which is insufficient for n=0 or n=1.
        # Accessing dp[1] or dp[2] before checking n<3 causes an IndexError.
        # Fix Hint: Allocate dp with length max(3, n+1) or handle base cases before assignments.
        # FIX: Handled base cases first to avoid IndexError and removed redundant array initialization.
        if n == 0: return 0
        if n == 1 or n == 2: return 1
        
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1
        for i in range(3, n + 1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        return dp[n]
        # Time Complexity: O(n) – each Tribonacci number up to n is computed once.
        # Space Complexity: O(n) – dp array stores n+1 integers.
        # Note: An optimal solution can reduce space to O(1) by using only three variables.

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna