class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # Your implementation is correct!
        # Time Complexity: O(n) - Each element is visited exactly once.
        # Space Complexity: O(1) - Excluding the output list, no extra space is used.
        # This is the optimal complexity for this problem.
        ans=[]
        i=0
        while i <len(nums):
            start=nums[i]

            while(i+1<len(nums) and nums[i]+1==nums[i+1]):
                i+=1
            
            if start==nums[i]:
                ans.append(f"{nums[i]}")

            else:
                ans.append(f"{start}->{nums[i]}")
            i+=1 # Ensure the pointer moves to the next potential range
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna