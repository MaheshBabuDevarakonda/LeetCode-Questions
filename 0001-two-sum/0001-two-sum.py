class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        num=[]
        dici={}
        for i in range(0,len(nums)):
            rem=target-nums[i]
            if rem in dici:
                return [dici[rem],i]
            dici[nums[i]]=i
        return num

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna