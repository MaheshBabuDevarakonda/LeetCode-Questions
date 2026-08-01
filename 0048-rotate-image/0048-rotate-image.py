class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row=len(matrix)
        col=len(matrix[0])
        mat = [[0] * col for _ in range(row)]
        for i in range(row):
            for j in range(i+1,row):
                matrix[i][j], matrix[j][i] = matrix[j][i],matrix[i][j]
        for i in range(row):
            for j in range(row//2):
                matrix[i][j],matrix[i][row-j-1]=matrix[i][row-j-1],matrix[i][j]
            



        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna