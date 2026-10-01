class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
        }
        for i in range(len(s)):
            if s[i] in pairs:
                if stack and stack[-1]==pairs[s[i]]:
                    stack.pop()
                else :
                    return False
            else:
                stack.append(s[i])
        return len(stack) == 0

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna