class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1=rec1[0]
        y1=rec1[1]
        x2=rec1[2]
        y2=rec1[3]
        x3=rec2[0]
        y3=rec2[1]
        x4=rec2[2]
        y4=rec2[3]

        return x1 < x4 and x3 < x2 and y1 < y4 and y3 < y2

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna