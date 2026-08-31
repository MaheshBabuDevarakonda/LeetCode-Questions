class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def slove(sub):
            if len(sub)==len(nums):
                ans.append(sub.copy())
            for num in nums:
                if num not in sub:
                    sub.append(num)
                    slove(sub)
                    sub.pop()
        slove([])
        return ans
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna