class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Coaching Analysis:
        # 1. Your current approach uses sorting, making the Time Complexity O(N log N).
        # 2. Space Complexity is O(1) or O(N) depending on the sorting implementation.
        # 3. BUG: 'if i+1 in nums' inside a loop creates O(N^2) complexity because 'in' on a list is O(N).
        # 4. BUG: Your logic doesn't handle duplicate numbers (e.g., [1, 2, 2, 3]).
        # 5. The optimal solution for this problem is O(N) time using a Hash Set.
        
        # Coach Note: Your current implementation is O(N^2) due to 'while a in nums' searching a list.
        # To achieve the optimal O(N) time complexity:
        # 1. Convert nums to a set: num_set = set(nums)
        # 2. Iterate through the set.
        # 3. Only start counting if (num - 1) is NOT in the set (this identifies the start of a sequence).
        # 4. Use a while loop to count the length of the sequence starting from that number.
        # 5. Update your max count.
        # This ensures each element is visited at most twice.
        
        n=len(nums)
        if n == 0: return 0 # Edge case: empty list
        nums.sort()
        mcount=0
        lsmallest=float("-inf")
        for i in range(n):
            num=nums[i]
            if num-1==lsmallest:
                count+=1
                lsmallest=num
            elif num!=lsmallest:
                count=1
                lsmallest=num
            mcount=max(mcount,count)
        return mcount
# Hint to improve:
# Try converting 'nums' into a set first. 
# Then, only start counting a sequence if 'num - 1' is NOT in the set.
# This ensures you only process each sequence once, achieving O(N) time.
# Check the "Video Solutions" tab in the LeetHub editor for a visual walkthrough!

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna