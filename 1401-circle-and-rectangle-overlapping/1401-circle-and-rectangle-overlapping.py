class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        closest_x=max(x1,min(xCenter,x2))
        closest_y=max(y1,min(yCenter,y2))

        # Calculate the squared distance
        distance_squared = (closest_x - xCenter)**2 + (closest_y - yCenter)**2

        # Compare it to the radius squared
        if distance_squared <= radius**2:
            return True
        return False    
    

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna