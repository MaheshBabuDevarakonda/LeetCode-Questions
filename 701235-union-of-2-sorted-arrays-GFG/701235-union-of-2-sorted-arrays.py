class Solution:
    def findUnion(self, a, b):
        d = {}
        for i in a:
            d[i] = 1

        for i in b:
            d[i] = 1

        return sorted(list(d.keys()))

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna