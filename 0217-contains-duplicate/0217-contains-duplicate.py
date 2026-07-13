class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dici={}
        for i in nums:
            if i not in dici:
                dici[i]=1
            else:
                dici[i]+=1
            if dici[i]==2:
                return True  # Fixed lowercase 'true' to uppercase 'True'
                break
        return False  # Fixed lowercase 'false' to uppercase 'False'

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna