import streamlit as st
from main import rockPaperScissorsGame

# Initialize game object
game = rockPaperScissorsGame()

# Page title and author
st.title("Rock Paper Scissors Game")
st.write("developed by Ermia Razavi")

# Input for player
player_choice = st.text_input("Enter rock, paper, or scissors:", key="player_choice")

# Generate computer choice
computer_choice = game.get_computer_choice()

# Button to play
submit_button = st.button("Play")



if submit_button:
    # Validate input
    if player_choice not in game.valid_choices:
        st.error("❌ Invalid choice. Please enter rock, paper, or scissors.")
    else:
        # Determine winner
        winner = game.specify_winner(player_choice, computer_choice)
        st.write(f"Player chose: {player_choice} | Computer chose: {computer_choice}")
        st.info(winner)
