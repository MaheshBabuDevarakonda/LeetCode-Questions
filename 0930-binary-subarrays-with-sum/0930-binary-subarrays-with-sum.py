class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # COACH: Your logic using the 'atmost(k) - atmost(k-1)' technique is correct!
        # This is a clever way to handle the 'exact' sum requirement using a sliding window.
        #
        # BUG ALERT: You have a variable naming inconsistency in your helper function.
        # Inside atmostk(nums, k), you are using 'goal' instead of the parameter 'k' 
        # in the while loop: 'while(temp > goal):'. This will cause incorrect results.
        #
        # Time Complexity: O(N) - Each element is visited at most twice by the pointers.
        # Space Complexity: O(1) - Only a few integer variables are used.
        # This is the optimal complexity for this problem.
        #
        # FIX: Change 'while(temp > goal):' to 'while(temp > k):'.
        def atmostk(nums,k):
            if k<0:
                return 0
            ans=0
            l=0
            temp=0
            for r in range(len(nums)):
                if nums[r]==1:
                    temp+=1
                while(temp>k): # Changed 'goal' to 'k' to correctly use the function parameter
                    if nums[l]==1:
                        temp-=1
                    l+=1
                ans+=r-l+1
            return ans
        return atmostk(nums,goal)-atmostk(nums,goal-1)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna