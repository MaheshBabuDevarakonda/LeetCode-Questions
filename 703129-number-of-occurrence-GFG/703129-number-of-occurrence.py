class Solution:
    def ub(self,arr,target):
        low=0
        high=len(arr)-1
        ub=-1
        while(low<=high):
            mid=(low+high)//2
            if arr[mid]==target:
                ub=mid
                low=mid+1
            elif arr[mid]>target:
                high=mid-1
            else:
                low=mid+1
        return ub
        
    def lb(self,arr,target):
        low=0
        high=len(arr)-1
        lb=-1
        while(low<=high):
            mid=(low+high)//2
            if arr[mid]==target:
                lb=mid
                high=mid-1
            elif arr[mid]>target:
                high=mid-1
            else:
                low=mid+1
        return lb
        
        
    def countFreq(self, arr, target):
        lb=self.lb(arr,target)
        ub=self.ub(arr,target)
        if lb==-1:
            return 0
        return ub-lb+1
        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna