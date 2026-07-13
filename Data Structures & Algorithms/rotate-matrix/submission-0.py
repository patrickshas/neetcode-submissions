class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # first: flip horizontally
        flipped = list(reversed(matrix))

        # second: transpose matrix
        rotated = list(map(list, zip(*flipped)))

        for i in range(len(matrix)):
            for j in range (len(matrix[0])):
                matrix [i][j] = rotated [i][j]