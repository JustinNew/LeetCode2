# 54. Spiral Matrix

# Google Tag

'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''

'''
Layer by layer
Be careful when finished one layer and go to next one
Be careful about edge case
'''

class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
       
        if len(matrix) == 0:
            return []
        
        if len(matrix) == 1:
            return matrix[0]
 
        m = len(matrix)
        n = len(matrix[0])
 
        i = 0
        j = 0
        res = []
        while m >= 2 and n >= 2:
 
            # Go right
            for c in range(n - 1):
                res.append(matrix[i][j])
                j += 1

            # Go down
            for c in range(m - 1):
                res.append(matrix[i][j])
                i += 1

            # Go left
            for c in range(n - 1):
                res.append(matrix[i][j])
                j -= 1

            # Go up
            for c in range(m - 1):
                res.append(matrix[i][j])
                i -= 1

            i += 1
            j += 1
            m -= 2
            n -= 2

        if m == 1:
            for c in range(n):
                res.append(matrix[i][j])
                j += 1
        elif n == 1:
            for c in range(m):
                res.append(matrix[i][j])
                i += 1

        return res 
