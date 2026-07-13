class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        n=len(nums)
        count=0
        for i in range(n):
            for  j in range(i+1,n):
                if nums[i]==nums[j]:
                    count+=1
        return count
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna