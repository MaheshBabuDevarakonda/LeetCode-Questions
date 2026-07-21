class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # Coaching Note: Your sliding window logic is almost perfect!
        # However, there is a small bug in your dictionary removal logic.
        ans=0
        l=0
        dici={}
        k=2
        for r in range(len(fruits)):
            a=fruits[r]
            if a  in dici:
                dici[a]+=1
            else:
                dici[a]=1
            while len(dici)>k :
                lval=fruits[l]
                dici[lval]-=1
                # BUG FOUND: You are popping the key when the count is 1.
                # You should pop the key ONLY when the count reaches 0.
                if dici[lval]==0: 
                    dici.pop(lval)
                l+=1
            ans=max(ans,r-l+1)
        return ans

# --- LeetHub AI Analysis ---
# Current Complexity:
# Time: O(N) - Each element is visited at most twice (once by r, once by l).
# Space: O(1) - The dictionary stores at most k+1 (3) elements.
# 
# Correction Hint: Change 'if dici[lval]==1:' to 'if dici[lval]==0:'.
# Once you fix this, your solution will be optimal.
# If you get stuck, check the "Video Solutions" tab in the LeetHub editor!

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna