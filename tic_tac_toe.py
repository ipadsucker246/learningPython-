# Another implementation of tic_tac_toe in python by me. Instead of using cases and biases, this implementation uses recursion, somewhat of an looping automata that plays itself to predict the best moves. 
import random
board = [0,1,2,3,4,5,6,7,8,9,]
turn = 0 
player_mark = ''
computer_mark = '' 

def make_move(board, index, mark): 
    # for better clarity, receives fake_board, index to mark, the mark(turn), then return a fake board to test with the move you're making 
    new_board = board
    new_board[index] = mark 
    return new_board

def copy(bo): 
    new_board = [] 
    for i in bo: 
        new_board.append(i)
    return new_board

def make_board(board): 
    #visually show the current board 
    print '\n'
    print str(board[1]) + '|' + str(board[2]) + '|' + str(board[3])
    print "------"
    print str(board[4]) + '|' + str(board[5]) + '|' + str(board[6])
    print "------"
    print str(board[7]) + '|' + str(board[8]) + '|' + str(board[9])
    print '\n'

def is_done(board):
    #check if the board is finished or not
    for i in range(1,10,3):
        if board[i] == board[i+1] and board[i+1] == board[i+2]: return 1 
    for i in range(1,4):
        if board[i] == board[i+3] and board[i+3] == board[i+6]: return 1
    if board[1] == board[5] and board[5] == board[9]: return 1 
    elif board[3] == board[5] and board[5] == board[7]: return 1  
    full = [i for i in board if i in range(1,10)]
    if len(full) == 0 : 
        return 3
    return 0


def is_free(board):
    counter = 0 
    for i in board: 
        if i in range(1,10): 
            counter += 1 
    if counter == 0: 
        return 0 
    elif counter > 0: 
        return 1 


def who_first(): 
    #prompts the player to know if he/she wants to go first or not 
    counter = 0 
    for i in range(4):   
        ask = str(raw_input("Do you wanna go first: "))
        if 'y' in ask.lower(): 
            turn = 2
            return turn 
        elif 'n' in ask.lower(): 
            turn = 3
            return turn 
        elif counter == 2: 
            print "IF you don't choose your turn now or the game will exit" 
        else: 
            print "I don't understand, please type in yes or no."

def what_mark(): 
     #prompts the player which marks he/she wants to be 
    counter = 0 
    for  i in range(4):   
        ask = str(raw_input("Do you wanna be 'X' or 'O': "))
        if 'x' in ask.lower(): 
            player_mark = 'X'
            return player_mark
        elif 'o' in ask.lower(): 
            player_mark = 'O'
            return player_mark
        elif counter == 2: 
            print "IF you don't choose your mark now, the game will exit"
        else: 
            print "I don't understand, please type in 'X' or 'O'."

def case_get_move(board, player_mark, computer_mark): 
    # very elementary, case_specific, use MINIMAAX instead.
    for i in range(1,10): 
        if i in board:
            new = copy(board)
            new[i] = computer_mark
            result = is_done(new)
            if result == 1: return i 
    
    for i in range(1,10): 
        if i in board:
            new = copy(board)
            new[i] = player_mark
            result = is_done(new)
            if result == 1: return i 



def case_random(board):  
    for i in board: 
        if i in[1,3,7,9]:
            return i 
    for i in range(1,10): 
        if i in board: return i 
    

    

def get_move(board, turn, player_mark, computer_mark):
    # 2 phases, 1st phase will check if there is a move that would win the game instantly if not, 2nd phase will check all the possible moves by using recursion 
    # phase 1: check if the next move will win you the board by iterating through every available moves 
    turn = turn 
    new_turn = 0 
    free_space = [] 
    for i in range(1,10): 
        fake_board = board 
        # check if that move will win 
        if i in fake_board: 
            fake_board = make_move(fake_board, i, turn, player_mark, computer_mark) 
            result = is_done(fake_board)
            # return 1 if win 
            if result == 1: 
                return i
            elif result == 0: 
                new_turn = turn + 1 
                free_space.append(i)
                return get_move(fake_board, new_turn, player_mark, computer_mark )
    return random.choice(free_space)
    # fix this function !!! 

# main game 

computer_mark = ''
    
player_mark = what_mark() 
if player_mark == None: end() 
    
turn = who_first()
if turn == None : end()

if player_mark == 'X': 
    computer_mark = 'O'
else:
    computer_mark = 'X'

make_board(board)

while True: 
    while turn % 2 == 0: 
        move = raw_input("Enter the move that you wanna play: ")
        if move not in "123456789":
            print "That move is invalid.\n"
        elif int(move) not in board: 
            print "That move is already taken."
        elif int(move) in board: 
            make_move(board, int(move), player_mark)
            make_board(board)
            result = is_done(board)
            if result == 0: 
                turn += 1 
            elif result == 1: 
                print " YOU WIN, WOW IS THIS EVEN POSSIBLE ?" 
                False 
            elif result == 3: 
                print 'DRAW!'
                False   

    while turn % 2 != 0: 
        print "Computer's turn"
        print '\n'
        move = case_get_move(board, player_mark, computer_mark)
        if move: 
            make_move(board, move,computer_mark)
            make_board(board)
            result = is_done(board)
            if result == 0: 
                turn += 1 
            elif result == 1: 
                print " YOU LOSE, DO  YOU THINK YOU CAN WIN ?" 
                False
            elif result == 3: 
                print 'DRAW!'
                False
        else: 
            move = case_random(board)
            make_move(board, move,computer_mark)
            make_board(board)
            result = is_done(board)
            if result == 0: 
                turn += 1 
            elif result == 1: 
                print " YOU LOSE, DO  YOU THINK YOU CAN WIN ?" 
                False 
            elif result == 3: 
                print 'DRAW!'
                False  
        




