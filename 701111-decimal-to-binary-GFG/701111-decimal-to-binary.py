class Solution:
    def decToBinary(self, n):
        result=""
        # code here
        while(n > 0):
            if n%2==1:
                result+="1"
            else:
                result+="0"
            n=n//2
        return result[::-1]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna