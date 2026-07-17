class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        cval=0
        left=0
        right=len(nums)-1
        while(left<right):
            cval+=int(str(nums[left])+str(nums[right]))
            left+=1
            right-=1
        if left==right:
            cval+=nums[left]
        return cval


            
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna