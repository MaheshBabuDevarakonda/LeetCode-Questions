class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans=float("inf")
        n=len(nums)
        l=0
        temp=0
        for r in range(len(nums)):
            temp+=nums[r]
            while(temp>=target):
                ans=min(ans,r-l+1)
                temp-=nums[l]
                l+=1
        if ans==float("inf"):
            return 0
        return ans
            

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna