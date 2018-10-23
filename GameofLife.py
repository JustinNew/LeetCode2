# 289. Game of Life

# Google Tag

'''
According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

Example:

Input: 
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output: 
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]

Follow up:

Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?
'''

# Pay attention as we use board itself as label.

class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        m = len(board)
        n = len(board[0])

        def countNeighbor(i, j):
            count = 0
            
            if i - 1 >= 0 and j - 1 >= 0 and board[i - 1][j - 1] % 10 == 1:
                count += 1
            if i - 1 >= 0 and board[i - 1][j] % 10 == 1:
                count += 1
            if i - 1 >= 0 and j + 1 < n and board[i - 1][j + 1] % 10 == 1:
                count += 1
            if i + 1 < m and j - 1 >= 0 and board[i + 1][j - 1] % 10 == 1:
                count += 1
            if i + 1 < m and board[i + 1][j] % 10 == 1:
                count += 1
            if i + 1 < m and j + 1 < n and board[i + 1][j + 1] % 10 == 1:
                count += 1
            if j - 1 >= 0 and board[i][j - 1] % 10 == 1:
                count += 1
            if j + 1 < n and board[i][j + 1] % 10 == 1:
                count += 1
                
            return count

        for k in range(m):
            for l in range(n):
                board[k][l] += 10 * countNeighbor(k, l)

        for k in range(m):
            for l in range(n):
                ppl = int(board[k][l] / 10)
                state = board[k][l] % 10

                if ppl < 2:
                    board[k][l] = 0
                elif ppl == 2:
                    board[k][l] = state
                elif ppl == 3:
                    board[k][l] = 1
                elif ppl > 3:
                    board[k][l] = 0

        return 
