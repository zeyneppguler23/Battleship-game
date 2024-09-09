from components import initialise_board, create_battleships, place_battleships

#It is anticipated that the coordinates argument will provide a tuple that shows the attack's row and column on the board. 
#To facilitate working with individual coordinates, the tuple is unpacked into distinct row and col variables in the next two lines.
#It is assumed that the coordinates parameter is a tuple with the x and y coordinates. 
#These coordinates are extracted by the function, which then turns them into integers and utilizes them to access the appropriate element on the board. 
#The coord variable holds the value at the given coordinates.

def attack(coordinate, board, battleships):
    if len(coordinate) != 2:
        raise ValueError("Invalid coordinates format")

    xcoor, ycoor = coordinate

    if 0 <= xcoor < len(board) and 0 <= ycoor < len(board):
        coord = board[xcoor][ycoor]
        if coord is None:
            print("Miss")
            return False, board, battleships
        else:
            name = coord
            battleships[name] -= 1
            print("hit")
            board[xcoor][ycoor] = None
            if battleships[name] == 0:
                print("the ship has sunk")
            return True, board, battleships
    else:
        raise ValueError("Coordinates out of range")

#create a function called cli_coordinates_input that takes no arguments 
def cli_coordinates_input():
#request the user to input coordinates for an attack 
# Get coordinates from the user
    latitude = int(input("Enter latitude: "))
    longitude = int(input("Enter longitude: "))
    coordinates = (latitude, longitude)
    return coordinates 


# Display the coordinates
#coordinates = cli_coordinates_input()
#print("Coordinates:", coordinates)

#simple game loop
def simple_game_loop():
  board = []
  battleships = {}  
  print("welcome to the battleships game!")
  board = initialise_board(size=10)
  battleships = create_battleships("battleships.txt")
  board = place_battleships(board, battleships)
  while any(value > 0 for value in battleships.values()):
      coordinates=cli_coordinates_input()
      hit, board, battleships = attack(coordinates,board,battleships)
  print("GAME OVER")

#simple_game_loop()
if __name__ == "__main__":
    attack()
    cli_coordinates_input()
    simple_game_loop()

    