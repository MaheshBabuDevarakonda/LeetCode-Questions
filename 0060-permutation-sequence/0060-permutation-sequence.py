class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fact=1
        numbers=[]
        for i in range(1,n):
            fact*=i
            numbers.append(i)
        numbers.append(n)

        k=k-1
        ans=""
        while True:
            ans+=str(numbers[k//fact])
            numbers.pop(k//fact)
            if len(numbers)==0:
                break
            k=k%fact
            fact=fact//len(numbers)
        return ans



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna