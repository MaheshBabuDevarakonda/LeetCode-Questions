class Solution:
    def digitsum(self,a):
        sum=0
        while(a!=0):
            rem=a%10
            sum+=rem
            a=a//10 # Hint: Use floor division (//) instead of (/) in Python to keep 'a' as an integer
        return sum
    def smallestIndex(self, nums: List[int]) -> int:
        # Current Time Complexity: O(n * log10(max_val))
        # Current Space Complexity: O(1)
        # This is optimal for this problem.
        
        # Bug 1: 'ans' is defined as a class variable. In LeetCode, 
        # it's better to define it locally inside the function.
        # Bug 2: In 'self.ans=min(ans,i)', 'ans' is not defined (should be self.ans).
        # Bug 3: The problem asks for the SMALLEST index. Since we iterate from 0 
        # upwards, the first time (curr == i) is True, that is your smallest index.
        
        for i in range(len(nums)):
            curr=self.digitsum(nums[i])
            if curr==i:
                return i # Return immediately to get the smallest index
        
        return -1 # Return -1 if no such index is found as per problem requirements

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna