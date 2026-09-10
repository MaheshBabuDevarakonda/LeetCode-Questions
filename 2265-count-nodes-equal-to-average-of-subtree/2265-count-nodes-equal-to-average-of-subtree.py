class Solution:

    def averageOfSubtree(self, root):
        if root is None:
            return 0

        count = 0

        subtree_sum = self.get_sum(root)
        subtree_count = self.get_count(root)

        if root.val == subtree_sum // subtree_count:
            count += 1

        count += self.averageOfSubtree(root.left)
        count += self.averageOfSubtree(root.right)

        return count

    def get_sum(self, root):
        if root is None:
            return 0

        return (
            root.val
            + self.get_sum(root.left)
            + self.get_sum(root.right)
        )

    def get_count(self, root):
        if root is None:
            return 0

        return (
            1
            + self.get_count(root.left)
            + self.get_count(root.right)
        )

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna