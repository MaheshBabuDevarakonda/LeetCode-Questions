class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # Coaching Analysis:
        # Current Logic: Sliding Window with frequency maps.
        # Time Complexity: O(N * 26) = O(N) where N is len(s).
        # Space Complexity: O(1) since the map size is capped at 26 characters.
        # Optimal Complexity: O(N) Time / O(1) Space.
        
        def dicicompare(dicia,dicib):
            if len(dicia)!=len(dicib):
                return False
            for  i in dicia:
                if i not in dicib or dicia[i]!=dicib[i]:
                    return False
            return True
        dicib={}
        dicia={}
        for i in p:
            if i in dicib:
                dicib[i]+=1
            else:
                dicib[i]=1
            
        l=0
        ans=[]
        n=len(s)
        k = len(p) # Hint: You used 'k' in the loop but didn't define it. Define k = len(p).
        for r in range(n): # Fix: Added 'in' keyword to 'for r range(n)'
            val=s[r]
            if val in dicia:
                dicia[val]+=1
            else:
                dicia[val]=1

            if r-l==k:
                lval=s[l]
                dicia[lval]-=1
                if dicia[lval]==0:
                    dicia.pop(lval)
                l+=1
            if r-l+1==k:
                if dicicompare(dicia,dicib):
                    ans.append(l)
        
        # Fix: The 'return ans' was inside the for-loop, causing it to exit after the first iteration.
        # Move it outside the loop to return the full list of indices.
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna