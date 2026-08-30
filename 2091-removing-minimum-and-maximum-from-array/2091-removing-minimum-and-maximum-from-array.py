class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:

        maximum = nums[0]
        minimum = nums[0]

        # Loop 1: Find min and max values
        for i in range(len(nums)):
            if nums[i] > maximum:
                maximum = nums[i]

            if nums[i] < minimum:
                minimum = nums[i]

        min_index = 0
        max_index = 0

        # Loop 2: Find indices
        for i in range(len(nums)):
            if nums[i] == minimum:
                min_index = i

            if nums[i] == maximum:
                max_index = i

        n = len(nums)

        # Both from left
        left = max(min_index, max_index) + 1

        # Both from right
        right = n - min(min_index, max_index)

        # One from left, one from right
        both = min(min_index, max_index) + 1 + n - max(min_index, max_index)

        return min(left, right, both)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna