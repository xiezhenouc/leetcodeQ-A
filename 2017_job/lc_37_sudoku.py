import datetime

'''
    isValidSudokuNext is very important
    I use isValidSudoku, execution time = 5s
    I use isValidSudokuNext, execution time = 0.5s
    Reasons:
 	isValidSudokuNext calculate very quick, because it judge only one element change
        isValidSudoku calculate whole board, so it is slower than isValidSudokuNext
      
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
                        n += 1
                    m += 1
                if not self.smallIsValid(mylist):
                    return False

        return True
    def produceCandidateSet(self, board):
        global flag
        myCandidateList = {}
        initMul = 1

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    curlist = []
                    for k in range(9):
                        board[i][j] = str(k+1) 
                        if self.isValidSudoku(board) == True:
                            curlist.append(str(k+1))
                        board[i][j] = '.'
 
                    if len(curlist) > 0:
                        initMul *= len(curlist)
                        #print i, j, ':', curlist, initMul
                        if len(curlist) == 1:
                            flag = 1
                            board[i][j] = curlist[0]
                        myCandidateList[str(i)+str(j)] = curlist
               
        #print 'last', '%E' % initMul
        return myCandidateList                  
 
    def solveSudokuPhase1(self, board):
        global flag

        myCandidateList = self.produceCandidateSet(board)
        myboard = board 

        flag = 0
        count = 0 
        while True:
            count += 1
            self.produceCandidateSet(myboard) 
            if flag == 0:
                print count
                break
            flag = 0
 
        for one in myboard:
            print ''.join(one)
        print ''
        return myCandidateList

    def isValidBoard(self, board):
        i = 0
        j = 0
        while i < 9:
            j = 0
            while j < 9:
                if board[i][j] == '.':
                        return False
                j += 1
            i += 1
        return True

    def isValidSudokuNext(self, x, y, board):
        i = 0
        while i < 9:
            if i != x and board[i][y] == board[x][y]:
                return False
            i += 1
        j = 0
        while j < 9:
            if j != y and board[x][j] == board[x][y]:
                return False;
            j += 1
        i = 3 * (x / 3) 
        while i < 3 * (x / 3 + 1):
            j = 3 * (y / 3)
            while j < 3 * (y / 3 + 1):
                if (i != x or j != y) and board[i][j] == board[x][y]:
                    return False;
                j += 1
            i += 1
        return True;

    def recursiveFunc(self, i, j, myCandidateList, board):
        global success

        #print 'current i, j:', i, j

        while i < 9:
            while j < 9:
                if board[i][j] == '.':
                    #print myCandidateList[str(i)+str(j)]

                    for one in myCandidateList[str(i)+str(j)]:
                        board[i][j] = str(one)
                        if self.isValidSudokuNext(i, j, board):
                            if j < 8:
                                nexti = i + 0
                                nextj = j + 1
                            else:
                                nexti = i + 1
                                nextj = 0
                            if self.recursiveFunc(nexti, nextj, myCandidateList, board):
                                return True
                        board[i][j] = '.'    
                    if board[i][j] == '.':
                        return False
                j += 1
            i += 1
            #initialization
            j = 0
        if self.isValidBoard(board) and self.isValidSudoku(board):
            return True
        else:
            return False
        

    def solveSudokuPhase2(self, board):
        myCandidateList = self.solveSudokuPhase1(board)
        print self.recursiveFunc(0, 0, myCandidateList, board)

        for one in board:
            print ''.join(one)

flag = 0
success = False

if __name__ == '__main__':
    '''
    board = [
                    list('53..7....'),
                    list('6..195...'),
                    list('.98....6.'),
                    list('8...6...3'),
                    list('4..8.3..1'),
                    list('7...2...6'),
                    list('.6....28.'),
                    list('...419..5'),
                    list('....8..79')
            ]
    '''
    #board = [list("..9748..."),list("7........"),list(".2.1.9..."),list("..7...24."),list(".64.1.59."),list(".98...3.."),list("...8.3.2."),list("........6"),list("...2759..")]
    board = [list(".....7..9"),list(".4..812.."),list("...9...1."),list("..53...72"),list("293....5."),list(".....53.."),list("8...23..."),list("7...5..4."),list("531.7....")]

    starttime = datetime.datetime.now()

    Solution().solveSudokuPhase2(board) 

    endtime = datetime.datetime.now()

    print endtime - starttime
    '''
    for one in result:
        print one, result[one]
    '''


