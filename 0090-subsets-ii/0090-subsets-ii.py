class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result=[]
        nums.sort()
        def slove(ind,sub):
            if ind==len(nums):
                result.append(sub.copy())
                return
            sub.append(nums[ind])
            slove(ind+1,sub)
            sub.pop()
            slove(ind+1,sub)
        slove(0,[])
        result = list(set(map(tuple, result)))
        result.sort()
        return [list(x) for x in result]
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna