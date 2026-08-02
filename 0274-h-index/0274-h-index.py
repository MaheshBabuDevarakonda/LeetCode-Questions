class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        hindex=0
        for i in citations:
            if i>hindex:
                hindex+=1
            else :
                return hindex
        return hindex


            

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna