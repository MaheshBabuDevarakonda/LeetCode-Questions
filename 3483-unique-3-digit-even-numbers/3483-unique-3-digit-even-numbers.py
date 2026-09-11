class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        ans = set()

        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):
                    
                    if i == j or j == k or i == k:
                        continue
                    
                    num = digits[i] * 100 + digits[j] * 10 + digits[k]

                    # 3-digit number cannot start with 0
                    # and must be even
                    if digits[i] != 0 and digits[k] % 2 == 0:
                        ans.add(num)

        return len(ans)
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna