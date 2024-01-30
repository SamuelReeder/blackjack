import game
# from flask import Flask, render_template, request, session


# app = Flask(__name__)
# app.secret_key = 'your_secret_key'  # Needed for session management

# @app.route('/')
# def index():
#     return render_template('index.html')  # The HTML template for the game

# @app.route('/play', methods=['POST'])
# def play():
#     # Game logic here
#     return 'Game state or response'


def main():
    print("Welcome to Blackjack")
    # app.run(debug=True)
    blackjack = game.Game(1)
    blackjack.play()
    

if __name__ == '__main__':
    main()