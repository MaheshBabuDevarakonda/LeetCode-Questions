class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        dici={}
        temp=97
        s=""
        for i in key:
            if i!=" " and i not in dici:
                dici[i]=chr(temp)
                temp+=1
        for i in message:
            if i==" ":
                s+=" "
            else:
                s+=dici[i]
        return s

            
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna