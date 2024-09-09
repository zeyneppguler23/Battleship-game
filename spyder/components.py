import random
import json

#create a function called initialise_board with a single argument, size, that has a default value 10 and returns a list of lists that represents the board state. 
#The initial board state should be empty so the list should be full of None values. 
def initialise_board(size=10):
    board = []
    for y in range (size):
        row = []
        for x in range(size):
            row.append(None)
        board.append(row)
    return board
#print(initialize_board())

#board = initialize_board()

#Create a function called create_battleships that takes one optional argument, filename, which has a default value “battleships.txt”. 
def create_battleships(filename= 'battleships.txt'):
    
    #The function should read the file and create a dictionary variable with the identifier, battleships
    # containing keys as the battleship name and the value as its size. 
    #split dictionary into keys and values
    battleships= {}
    with open('battleships.txt') as item:
        ships = item.readlines()
        for i in ships:
            (name, size) = i.split(":")
            battleships[name]= int(size.strip())
        #print(battleships)
        return battleships
#battleships=create_battleships(filename= 'battleship.txt')
    
#Create a function called place_battleships with two arguments, board and ships.
#The board argument should be a list of lists that was returned from an initialise_board function call,
#ships should be a dictionary that was returned from a create_battleships function call.


#This assumes your board is a 2D list 
#Starting from the supplied row and column, the function moves the battleship in the specified direction.

def place_battleships(board = initialise_board(), ships = create_battleships(), algorithm="simple"):
    #Placing battleships on board and updating the board.
    #Simple - Placing each battleship horizontal on a new rows starting from (0,0)
    #Random - Placing the battleships in random positions and orientations.'''
    # The function place_battleships takes three parameters: board, battleships, and algorithm
    #print(algorithm)
    if algorithm == "simple":
        count =0
        for name, size in ships.items():
            placed = False
            while not placed:
                try:
                    row = count
                    count=count +1 
                    col = 0
                    #print(board)
                    for i in range(size):
                        #print(row, col + i)
                        if board[row][col + i] is not None:
                              raise ValueError("Ship overlap detected.")
                        #Checks for overlap with existing ships on the board. When overlap is identified, a ValueError is thrown.
                    for i in range(size):
                        board[row][col + i] = name
                    placed = True
                    #Checks for overlap with existing ships on the board. When overlap is identified, a ValueError is thrown.
                except ValueError:
                    print("ValueError")
    elif algorithm == "random":
        for name, size in ships.items():
            placed = False
            while not placed:
                overlap=True
                while overlap == True:
                    row = random.randint(0, 9)
                    col = random.randint(0, 9 - (size + 1))
                    #print(board)
                    overlap = False
                    for i in range(size):
                        #print(row, col + i)
                        overlap=False
                        if board[row][col + i] is not None:
                            overlap= True
                for i in range(size):
                    board[row][col + i] = name
                if overlap == False:
                    placed = True
    elif algorithm == "custom":
            custom_placement_pre = {}
            with open("placement.json", "r") as place:
                custom_placement_pre = json.load(place)
            for name, value in custom_placement_pre.items():
                placed = False
                while not placed:
                    try:
                        row = int(value[0])
                        col = int(value[1])  
                        rot = value[2]
                        size = ships[name] 
                        if rot == "h":
                            for i in range(size): 
                                if board[row][col + i] is not None:
                                    raise ValueError("Ship overlap")
                            for i in range(size):
                                board[row][col + i] = name
                            placed = True
                        elif rot == "v":
                            for i in range(size):
                                if board[row + i][col] is not None:
                                    raise ValueError("Ship overlap detected.")
                            for i in range(size):
                                board[row + i][col] = name
                            placed = True
                    except:
                        raise ValueError("loop error")
    else:
        raise ValueError("inappopriate algorithm")
    return board
                    
      

board= initialise_board()
battleships=create_battleships()
#place_battleships(board, battleships, algorithm="simple")
#place_battleships(board, battleships, algorithm="random")
#place_battleships(board, battleships, algorithm="custom")
if __name__ == "__main__":
    initialise_board()
    create_battleships()
    place_battleships()




