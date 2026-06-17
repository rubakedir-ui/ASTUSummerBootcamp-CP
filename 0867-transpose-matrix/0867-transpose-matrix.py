class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        row = len(matrix)
        colm = len(matrix[0])

        result = []

        for c in range(colm):
            new_row = []

            for r in range(row):
                   new_row.append(matrix[r][c])

            result.append(new_row)

        return result