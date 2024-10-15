import random


board = [' ' for _ in range(9)]


def insertLetter(letter, pos):
    board[pos] = letter


def spaceIsFree(pos):
    return board[pos] == ' '


def printBoard(board):
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('-----------')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('-----------')
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])


def isBoardFull(board):
    return board.count(' ') == 0


def isWinner(bo, le):
    return ((bo[0] == le and bo[1] == le and bo[2] == le) or
            (bo[3] == le and bo[4] == le and bo[5] == le) or
            (bo[6] == le and bo[7] == le and bo[8] == le) or
            (bo[0] == le and bo[3] == le and bo[6] == le) or
            (bo[1] == le and bo[4] == le and bo[7] == le) or
            (bo[2] == le and bo[5] == le and bo[8] == le) or
            (bo[0] == le and bo[4] == le and bo[8] == le) or
            (bo[2] == le and bo[4] == le and bo[6] == le))


def minimax(board, depth, isMaximizing):
    if isWinner(board, 'X'):
        return -10
    elif isWinner(board, 'O'):
        return 10
    elif isBoardFull(board):
        return 0

    if isMaximizing:
        bestScore = -1000
        for i in range(9):
            if spaceIsFree(i):
                insertLetter('O', i)
                score = minimax(board, depth + 1, False)
                insertLetter(' ', i)
                bestScore = max(score, bestScore)
        return bestScore
    else:
        bestScore = 1000
        for i in range(9):
            if spaceIsFree(i):
                insertLetter('X', i)
                score = minimax(board, depth + 1, True)
                insertLetter(' ', i)
                bestScore = min(score, bestScore)
        return bestScore


def alphaBeta(board, depth, alpha, beta, isMaximizing):
    if isWinner(board, 'X'):
        return -10
    elif isWinner(board, 'O'):
        return 10
    elif isBoardFull(board):
        return 0

    if isMaximizing:
        bestScore = -1000
        for i in range(9):
            if spaceIsFree(i):
                insertLetter('O', i)
                score = alphaBeta(board, depth + 1, alpha, beta, False)
                insertLetter(' ', i)
                bestScore = max(score, bestScore)
                alpha = max(alpha, bestScore)
                if beta <= alpha:
                    break
        return bestScore
    else:
        bestScore = 1000
        for i in range(9):
            if spaceIsFree(i):
                insertLetter('X', i)
                score = alphaBeta(board, depth + 1, alpha, beta, True)
                insertLetter(' ', i)
                bestScore = min(score, bestScore)
                beta = min(beta, bestScore)
                if beta <= alpha:
                    break
        return bestScore


def compMove():
    bestScore = -1000
    bestMove = 0
    for i in range(9):
        if spaceIsFree(i):
            insertLetter('O', i)
            score = alphaBeta(board, 0, -1000, 1000, False)
            insertLetter(' ', i)
            if score > bestScore:
                bestScore = score
                bestMove = i
    insertLetter('O', bestMove)
    return


def playerMove():
    run = True
    while run:
        move = input("Please select a position to place an 'X' (1-9): ")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move - 1):
                    run = False
                    insertLetter('X', move - 1)
                else:
                    print("Sorry, this space is occupied!")
            else:
                print("Please type a number within the range!")
        except:
            print("Please type a number!")


def main():
    print("Welcome to Tic Tac Toe!")
    printBoard(board)

    while not(isBoardFull(board)):
        if not(isWinner(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print("Sorry, O's won this time!")
            break

        if not(isWinner(board, 'X')):
            compMove()
            printBoard(board)
        else:
            print("X's won this time! Good Job!")
            break

    if isBoardFull(board):
        print("Tie Game!")

if __name__ == "__main__":
    main()