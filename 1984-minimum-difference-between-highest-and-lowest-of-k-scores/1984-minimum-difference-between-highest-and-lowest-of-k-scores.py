class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans=float("inf")
        l=0
        for r in range(len(nums)):
            if(r-l==k):
                l+=1
            if(r-l+1==k):
                ans=min(ans,nums[r]-nums[l])
        return ans
                


        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna