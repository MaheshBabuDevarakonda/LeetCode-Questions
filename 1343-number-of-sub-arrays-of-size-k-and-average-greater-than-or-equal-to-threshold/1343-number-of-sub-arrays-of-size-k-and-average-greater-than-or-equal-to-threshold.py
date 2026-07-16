class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l=0
        count=0
        sum=0
        for r in range(len(arr)):
            sum+=arr[r]
            if(r-l==k):
                sum-=arr[l]
                l+=1
            if(r-l+1==k):
                if(sum//k>=threshold):
                    count+=1
        return count


            

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna