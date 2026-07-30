class Solution:
    def insertionSort(self, arr):
        # code here
        n=len(arr)
        for i in range(1,n):
            key=arr[i]
            j=i-1
            while(j>=0 and  arr[j]>key):
                arr[j+1]=arr[j]
                j-=1
            arr[j+1]=key
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna