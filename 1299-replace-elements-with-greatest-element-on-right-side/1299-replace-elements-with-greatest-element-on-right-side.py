class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n=len(arr)
        rmax=arr[n-1]
        for i in range(n-1,-1,-1):
            temp=arr[i]
            arr[i]=rmax
            rmax=max(rmax,temp)
        arr[n-1]=-1
        return arr


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna