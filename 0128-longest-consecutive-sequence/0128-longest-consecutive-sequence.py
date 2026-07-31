class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Current Time Complexity: O(n) - Each element is visited at most twice.
        # Current Space Complexity: O(n) - To store the set of numbers.
        # This is the optimal complexity for this problem!
        
        myset=set()
        n=len(nums)
        longest=0
        count=0

        for i in range(n):
            myset.add(nums[i])

            
        for num in myset:
            if num-1 not in myset:
                x=num
                count=1
                # BUG FOUND: The condition 'while x+1 not in myset' is inverted.
                # It should be 'while x+1 in myset' to continue the sequence.
                while x+1  in myset:
                    count+=1
                    x+=1
                longest=max(longest,count)
        
        # BUG FOUND: You are returning 'count' (the last sequence length) 
        # instead of 'longest' (the maximum length found).
        return longest

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna