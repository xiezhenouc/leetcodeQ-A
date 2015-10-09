'''
valid sudoku
'''
class Solution(object):
    def smallIsValid(self, listone):
        mydict = {}
        for one in listone:
            if one == '.':
                continue
            if one in mydict.keys():
                return False
            mydict[one] = one
        return True

    def isValidSudoku(self, board):
        #rows, cols
        for i in range(9):
            mylistrow = []
            mylistcol = []
            for j in range(9):
                mylistrow.append(board[i][j])
                mylistcol.append(board[j][i])
            if not self.smallIsValid(mylistrow) or not self.smallIsValid(mylistcol):
                return False
        #little square
        square = [0, 3, 6]
        for i in square:
            for j in square:
                m = i
                n = j
                mylist = []
                while m < i + 3:
                    n = j
                    while n < j + 3:
                        mylist.append(board[m][n])
                        print board[m][n],
                        n += 1
                    print ' '
                    m += 1

                print '---'
                if not self.smallIsValid(mylist):
                    return False

        return True



if __name__ == '__main__':
    board = [
                [5, 3, ".", ".", 7, ".", ".", ".", "."],
                [6, ".", ".", 1, 9, 5, ".", ".", "."],
                [".", 9, 8, ".", ".", ".", ".", 6, "."],
                [8, ".", ".", ".", 6, ".", ".", ".", 3],
                [4, ".", ".", 8, ".", 3, ".", ".", 1],
                [7, ".", ".", ".", 2, ".", ".", ".", 6],
                [".", 6, ".", ".", ".", ".", 2, 8, "."],
                [".", ".", ".", 4, 1, 9, ".", ".", 5],
                [".", ".", ".", ".", 8, ".", ".", 7, 9]
            ]
    print Solution().isValidSudoku(board)
