import json
import random
from flask import Flask, render_template, request, jsonify, session
from components import initialise_board, create_battleships, place_battleships
from game_engine import attack
from mp_game_engine import generate_attack, ai_opponent_game_loop
#In this module you should create two functions to handle the two webpage interfaces. 
#In the global namespace you should also create an app variable from the Flask object and 
#initiate the application from the if __name__=='__main__' block using app.run() 
#There will be two main webpages for our interface, the Battleships Placement page, and, the Gameplay page.  
#player
player_board = initialise_board()
player_ships = create_battleships("battleships.txt")
players = {}
players["Player"] = [player_board, player_ships]
user_board = initialise_board()
user_battleships = create_battleships()
ai_board = initialise_board()
ai_battleships = create_battleships()
ai_board = place_battleships(ai_board, ai_battleships, "random")
players["AI"] = [ai_battleships, ai_board]
players["Player"] = [user_board, user_battleships]
ships = create_battleships()
ship_sizes = create_battleships()
place_battleships_custom = place_battleships


#Battleship Placement page
#Create a function called placement_interface with a Flask decorator to map the /placement url endpoint. 
#In this function you must return a call to the Flask function render_template and use the placement.
app = Flask(__name__)
app.secret_key = 'session'
    


@app.route('/placement', methods=['GET', 'POST'])
def placement_interface():
    #get
    if request.method == "GET":
        ships = create_battleships()
        session['ships'] = ships
        return render_template('placement.html', ships=ships, board_size=10)
    
    #post
    elif request.method == "POST":
        data = request.get_json()
        session['data'] = data
        return jsonify({'message': 'Received'}), 200

def player_board_placement(board,battle_ships,ships): #Function for the flask app similar to custom algorithm
    custom_placement_pre = ships
    for name, value in custom_placement_pre.items():
        placed = False
        while not placed:
            try:
                row = int(value[1])
                col = int(value[0])   
                rot = value[2]
                size = battle_ships[name] 
                if rot == "h":
                    for i in range(size): 
                        if board[row][col + i] is not None:
                            raise ValueError("Ship overlap detected.")
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
                raise ValueError("value error") 
    return board

#Gameplay Page 
@app.route('/',methods=['GET', 'POST'])
def root():
    player_board = players["Player"][0]
    #implement the same in the mp_game_engine function
    ai_board = initialise_board()
    ai_battleships = create_battleships()
    ai_board = place_battleships(ai_board, ai_battleships, "random")  #AI placement
    
    if request.method == "GET":
        data = session.get('data')
        user_battle_ships = session.get('ships')
        user_board = player_board_placement(player_board, user_battle_ships, data)
        session["player_board"] = player_board
        session["user_battle_ships"] = user_battle_ships
        session["ai_board"]= ai_board
        session["ai_battleships"] = ai_battleships
        return render_template('main.html', player_board= user_board)


#Attack Route
@app.route("/attack", methods=["GET"])
def game_attack():
    
    # Extract values from session
    user_board, user_battle_ships, ai_board, ai_battleships = (
        session.get('player_board'),
        session.get('user_battle_ships'),
        session["ai_board"],
        session["ai_battleships"],
    )

    # Update session with new values
    session.update({
        "player_board": user_board,
        "user_battle_ships": user_battle_ships,
        "ai_board": ai_board,
        "ai_battleships": ai_battleships,
    })


    if request.method=="GET":
        #Getting coordinates
        x = request.args.get('x')
        y = request.args.get('y')
        coordinates = (int(y),int(x)) 
        #to create an AI's attack
        x, y = generate_attack()
        #to show AI's turn
        AI_Turn = (y,x)
        #AI's attack
        hit, ai_board, ai_battle_ships = attack(coordinates, ai_board, ai_battleships) #User's attack
        #board = ai_board 
        #battleships = ai_battleships 
        #player_result = attack(coordinates, board, battleships)
        #if player_result == True:
            #player_text = "hit"
        #else:
                #player_text = "missed"
        #check if game has finished
        #if all(value == 0 for value in player_ships.values()) or all(value == 0 for value in ai_battleships.values()):
                #gamefinished = 1
        #update sessions
    def update_session():
        session["ai_board"] = ai_board
        session["ai_battleships"] = ai_battleships
        session["player_board"] = player_board
        session["user_battle_ships"] = user_battle_ships

    def game_result_message(winner):
        if winner == 'player':
            return 'Game Over - You Win'
        elif winner == 'AI':
            return 'GAME OVER - You lost'
        else:
            raise ValueError("Invalid winner value")

    # Game Loop
    if any(value != 0 for value in user_battle_ships.values()) and any(value != 0 for value in ai_battleships.values()):
        if hit:
            update_session()
            return jsonify({'hit': True, 'AI_Turn': AI_Turn})
        else:
            update_session()
            return jsonify({'hit': False, 'AI_Turn': AI_Turn})
    else:
        winner = 'player' if all(user_battle_ships.values()) != 0 else 'AI' if all(ai_battleships.values()) != 0 else None
        return jsonify({'hit': hit, 'AI_Turn': AI_Turn, 'finished': game_result_message(winner)})

    hit, user_board, user_battle_ships = attack(AI_Turn, user_board, user_battle_ships)  # AI attack



           
        
    
    #The game is not finished
    # Example Not Finished Response
    #return jsonify({'hit': True,
        #'AI_Turn': (x,y)
       # })
    #The template expects a JSON response containing: hit = A boolean (true/false) value detailing whether the players coordinated hit an I ship or not. 
    # True if it was a hit.
    


if __name__ == '__main__':
    app.template_folder = "templates" #Where template html files are at
    app.run()
    