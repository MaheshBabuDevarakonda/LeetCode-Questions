class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        dici={}
        for i in nums:
            if i not in dici:
                dici[i]=1
            else:
                dici[i]=dici[i]+1
        for i in dici:
            if dici[i]>=n/2:
                return i
        return 0

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna