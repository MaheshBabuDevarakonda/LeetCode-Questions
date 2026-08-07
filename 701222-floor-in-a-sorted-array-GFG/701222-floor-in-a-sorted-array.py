class Solution:
    def findFloor(self, arr, x):
        n=len(arr)
        ans=n
        for i in range(n - 1, -1, -1):
            if arr[i] <= x:
                return i
        return -1
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna