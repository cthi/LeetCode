class Solution(object):

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        res = self.binsearch_1(0, len(matrix) - 1, matrix, target)

        if res is None:
            return True
        elif res - 1 < 0 or res - 1 >= len(matrix):
            return False
        else:
            row = matrix[res - 1]
            return self.binsearch_2(0, len(row) - 1, row, target)

    def binsearch_1(self, start, end, matrix, target):
        if start > end:
            return start
        else:
            middle = (start + end) // 2

            if matrix[middle][0] == target:
                return None
            elif matrix[middle][0] > target:
                return self.binsearch_1(start, middle - 1, matrix, target)
            else:
                return self.binsearch_1(middle + 1, end, matrix, target)

    def binsearch_2(self, start, end, arr, target):
        if start > end:
            return False
        else:
            middle = (start + end) // 2

            if arr[middle] == target:
                return True
            elif arr[middle] > target:
                return self.binsearch_2(start, middle - 1, arr, target)
            else:
                return self.binsearch_2(middle + 1, end, arr, target)
