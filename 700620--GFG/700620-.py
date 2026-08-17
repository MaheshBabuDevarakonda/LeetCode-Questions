# Your logic is correct! You've used a Hash Map (dictionary) to track the index of visited nodes.
# When a node is revisited, the difference between the current index and the stored index gives the loop length.
# Time Complexity: O(N) - Each node is visited once.
# Space Complexity: O(N) - In the worst case, all nodes are stored in the dictionary.
# Optimal Approach: You can achieve O(1) Space Complexity using Floyd's Cycle-Finding Algorithm (Tortoise and Hare).
# Hint: Use two pointers (slow and fast). Once they meet, keep one fixed and move the other until it meets the fixed one again, counting the steps.
# Since your current solution is correct and passes, you can submit it, but I recommend trying the two-pointer approach for better space efficiency!

class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None

class Solution:
    def lengthOfLoop(self, head):
        dici={}
        temp=head
        travel=0
        while(temp is not None):
            if temp in dici:
                return travel-dici[temp]
            dici[temp]=travel
            travel+=1
            temp=temp.next
        return None

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna