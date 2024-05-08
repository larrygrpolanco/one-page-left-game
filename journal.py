# === Game Design ===
# Step 3: Understand and define game mechanics
# - Clearly define how dice rolls, character creation, journaling, and end-game conditions work

# Step 4: Design the UI layout
# - Sketch out a preliminary design of the UI, focusing on usability and game flow

# === UI ===
# Implement the basic UI setup

# - Create the main window
import tkinter as tk

root = tk.Tk()
root.title("ONE PAGE LEFT - Horror Survival RPG")

# - Add a Text widget for the journal
text_widget = tk.Text(root, height=20, width=60)
text_widget.pack(pady=20)

# - Add buttons for game actions (e.g., roll dice, restart game)
button_frame = tk.Frame(root)
button_frame.pack()

roll_dice_button = tk.Button(button_frame, text="Roll Dice")
roll_dice_button.pack(side=tk.LEFT, padx=10)

restart_game_button = tk.Button(button_frame, text="Restart Game")
restart_game_button.pack(side=tk.LEFT, padx=10)


# === Game Logic ===
import random

# - Dice roll functionality
def roll_dice():
    return random.randint(1, 6)


# - Character and killer creation logic
character_archetypes = {
    1: {1: "Actor", 2: "Artist", 3: "Beat Cop", 4: "Bully", 5: "Cashier", 6: "CEO"},
    2: {
        1: "Clown",
        2: "Conman",
        3: "Convict / Felon",
        4: "Delivery Person",
        5: "Detective",
        6: "Drug Dealer",
    },
    3: {
        1: "Escort",
        2: "Exorcist",
        3: "Ghost Hunter",
        4: "Goth",
        5: "Hitchhiker",
        6: "Horror Writer",
    },
    4: {
        1: "Influencer",
        2: "IT / Programmer",
        3: "Janitor",
        4: "Jock",
        5: "Journalist",
        6: "Nun / Monk",
    },
    5: {
        1: "Nurse / Doctor",
        2: "Office Worker",
        3: "Paramedic",
        4: "Politician",
        5: "Preacher",
        6: "Private Eye",
    },
    6: {
        1: "Psychiatrist",
        2: "Psychic",
        3: "Socialite",
        4: "Taxi Driver",
        5: "Teacher",
        6: "Thief",
    },
}


# Function to get the character archetype based on dice rolls
def get_archetype(roll1, roll2):
    return character_archetypes[roll1][roll2]


# - Game progression logic based on the rules

# Step 7: Integrate LLM for story generation
# - Implement function to fetch story elements from LLM
# - Handle and parse LLM responses and integrate them into the game

# === Testing and Iteration ===
# Step 8: Perform functional testing
# - Test UI interactions
# - Test dice rolling mechanics and journal updates

# Step 9: Perform gameplay testing
# - Play the game to see how the mechanics and story unfold
# - Adjust game logic and UI based on gameplay experience

# Step 10: Collect user feedback (if possible)
# - Use feedback to refine game mechanics and UI

# === Finalization ===
# Step 11: Polish the UI
# - Refine the UI based on test and user feedback

# Step 12: Write documentation
# - Create simple documentation on how to install and play the game

# Step 13: Prepare for distribution
# - Package the game for distribution if planning to share it

# Run the tkinter main loop
root.mainloop()
