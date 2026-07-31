class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # Current Complexity: Time O(n), Space O(n)
        # Optimal Complexity: Time O(n), Space O(n)
        
        # ISSUE 1: 'ans' is initialized as an empty list []. 
        # You cannot assign values to indices that don't exist (e.g., ans[j] = ...).
        # FIX: Initialize 'ans' with placeholders: ans = [0] * n
        n=len(nums)
        j=0
        k=n//2
        pl=[]
        nl=[]
        ans=[]
        for i in range(n):
            if nums[i]>0:
                pl.append(nums[i])
            else:
                nl.append(nums[i])
        for i in range(len(pl)):
            ans.append(pl[i])
            ans.append(nl[i])
        return ans



# COACH TIP: 
# Your logic of splitting the array into two halves (positive and negative) 
# is interesting, but it assumes the first n/2 elements are positive 
# and the next n/2 are negative, which isn't true.
#
# HINT: Try using two pointers: 
# one starting at index 0 (for positives) and one at index 1 (for negatives).
# Increment each pointer by 2 every time you place an element.
#
# If you get stuck, check the "Video Solutions" tab in the LeetHub editor!

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna