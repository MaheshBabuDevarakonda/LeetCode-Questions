class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_odd = float('inf')

        for x in nums1:
            if x % 2 != 0:
                min_odd = min(min_odd, x)

        # If there is no odd number, everything is already even
        if min_odd == float('inf'):
            return True

        for x in nums1:
            if x % 2 == 0 and x < min_odd:
                return False

        return True

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna