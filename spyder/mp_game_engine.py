from components import initialise_board, create_battleships, place_battleships
from game_engine import attack, cli_coordinates_input
import random

#Store the username of each player as the key and their board and battleships as the value.
players= {}

def add_player(username, board, battleships):
    players[username] = (board, battleships)

#Create a function called generate_attack that returns a tuple with coordinates that can be passed to the attack function. 
#The coordinate produced by this function should change each time the function is called and should always be within the size of the board in play.

def generate_attack():
  x, y = random.randint(0,9), random.randint(0,9)
  tuple = (x,y)
  return tuple

#Create a function called ai_opponent_game_loop
def ai_opponent_game_loop(players = players):
    #Start the game with a welcome message.
    print("welcome to the game!")
    #Initialise two players in the dictionary, create their battleships and board. 
    #One player will be the user and the second player will be the AI opponent. 
    user_board = initialise_board()
    user_battleships = create_battleships()
    ai_board = initialise_board()
    ai_battleships = create_battleships()
    
    players["AI"] = [ai_battleships, ai_board]
    players["Player"] = [user_board, user_battleships]
    
    #Place the battleships using the random placement algorithm for the AI opponent and custom placement algorithm for the user. 
    ai_board = place_battleships(algorithm="random")
    user_board = place_battleships(algorithm="custom")
    #Prompt the user to take their turn and input the coordinates of their attack.
    hit = True
    gamefinished = 0 #to check if the play is still going... 
        
    while gamefinished == 0: #To check if the game is still going
        if all(value == 0 for value in user_battleships.values()) or all(value == 0 for value in ai_battleships.values()):
             gamefinished = 1 #means game has just finished
             break
        coordinates = cli_coordinates_input() #asking prompt for longitude and latitute values
        hit, ai_board, ai_battleships = attack(coordinates, ai_board , ai_battleships)
        
        coordinates = generate_attack()
        ai_hit, user_board , user_battleships = attack(coordinates, user_board, user_battleships)
        print(ascii(user_board))
          
    if user_battleships.values() == 0: #means that the play has finished
        print("Game Over! You Lost :( - sorry buddy") 
        
    elif ai_battleships.values()== 0: 
            print("Game Over! You Win")

   
if __name__ == "__main__":
    generate_attack()
    ai_opponent_game_loop()
      


    
