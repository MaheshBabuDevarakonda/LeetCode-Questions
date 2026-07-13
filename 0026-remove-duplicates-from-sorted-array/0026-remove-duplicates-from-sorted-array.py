class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Handles empty list edge case.
        s=set()
        j=0
        for i in nums:
            if i not in s:
                s.add(i)
                nums[j]=i
                j+=1
        return j

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna