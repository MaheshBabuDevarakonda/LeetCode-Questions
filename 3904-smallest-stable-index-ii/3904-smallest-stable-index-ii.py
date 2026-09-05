class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        maxarray=[0]*n
        minarray=[0]*n
        maxarray[0]=nums[0]
        minarray[n-1]=nums[n-1]
        ans=-1
        for i in range(1,len(nums)):
            maxarray[i]=max(nums[i],maxarray[i-1])
        for i in range(n-2,-1,-1):
            minarray[i]=min(minarray[i+1],nums[i])
        for i in range(len(nums)):
            if maxarray[i]-minarray[i]<=k:
                return i
        return -1


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna