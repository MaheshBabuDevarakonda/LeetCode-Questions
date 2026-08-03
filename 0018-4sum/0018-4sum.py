class Solution:
    def fourSum(self, nums, target):
        ans = []
        res = set()
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                hset = set()

                for k in range(j + 1, n):

                    f = target - (nums[i] + nums[j] + nums[k])

                    if f in hset:
                        t = sorted([nums[i], nums[j], nums[k], f])
                        res.add(tuple(t))

                    hset.add(nums[k])

        for x in res:
            ans.append(list(x))

        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna