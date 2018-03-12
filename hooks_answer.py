import itertools
# first create a 2d array 
w, h = 4,4 

board_rows = [[0 for i in range(w)] for i in range(h)] 

# for better visual representations 

# create a board for columns 

board_columns = [[row[i] for row in board_rows] for i in range(len(board_rows))]

# now we have to map our clues to their respective rows and columns

clues_columns = {0: 16, 1: 4, 2: 6, 3: 12}
cluse_rows = {0: 12, 1: 8,  2: 3, 3: 16}

# now we take into account all the possibilities of the outer hooks

outer = itertools.product([0,-1], repeat = 2)

for i in outer : print i

# next, we correlate to the respective clues of the "hooks" Ex: hook(0, 0) would