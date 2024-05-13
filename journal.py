import random
import tkinter.simpledialog as simpledialog
from tkinter import *
from tkinter import ttk

# from tkinter import StringVar
from rules import (
    character_archetypes,
    character_secrets,
    killer_masks,
    killer_weapons,
    killer_traits,
    journal_prompts,
)

# === Game Design ===
# Step 3: Understand and define game mechanics
# - Clearly define how dice rolls, character creation, journaling, and end-game conditions work

# Step 4: Design the UI layout
# - Sketch out a preliminary design of the UI, focusing on usability and game flow


# === Character and killer creation ====

roll_counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

luck = 1
favorite_number = 3  # Place holder


def roll_two_dice():
    return random.randint(1, 6), random.randint(1, 6)


def set_game_data():  # Function to get the character archetype based on dice rolls
    roll1, roll2 = roll_two_dice()
    game_data["character"]["archetype"] = character_archetypes[roll1][roll2]
    roll1, roll2 = roll_two_dice()
    game_data["character"]["secret"] = character_secrets[roll1][roll2]
    roll1, roll2 = roll_two_dice()
    game_data["killer"]["mask"] = killer_masks[roll1][roll2]
    roll1, roll2 = roll_two_dice()
    game_data["killer"]["weapon"] = killer_weapons[roll1][roll2]
    roll1, roll2 = roll_two_dice()
    game_data["killer"]["trait"] = killer_traits[roll1][roll2]


game_data = {
    "character": {"archetype": None, "secret": None},
    "killer": {"mask": None, "weapon": None, "trait": None},
}

entry_count = 0
max_entries = 8


def update_journal(text):
    global entry_count
    if entry_count < max_entries:
        journal.config(state=NORMAL)
        journal.insert(END, text + "\n")
        journal.config(state=DISABLED)
        journal.yview(END)
        entry_count += 1
    else:
        prompt_label.config(text="You have run out of space in your journal.")


def submit_entry():
    if entry_count < max_entries:
        entry_text = journal_entry.get()
        update_journal(entry_text)
        journal_entry.delete(0, END)
        prompt_label.config(text="Roll dice to continue...")
    else:
        prompt_label.config(text="No more entries allowed.")


def update_journal(text):
    journal.config(state=NORMAL)  # Enable text widget for editing
    journal.insert(END, text + "\n")  # Append text
    journal.config(state=DISABLED)  # Disable text widget to prevent user editing
    journal.yview(END)  # Auto-scroll to the end


def apply_luck_modifier(current_roll):
    global luck
    if luck > 0:
        modify = simpledialog.askstring(
            "Modify Roll", "Do you want to use 1 luck point to modify your roll? (y/n):"
        )
        if modify and modify.lower() == "y":
            modify_type = simpledialog.askstring(
                "Increase or Decrease",
                "Type 'increase' to add 1 or 'decrease' to subtract 1:",
            )
            if modify_type and modify_type.lower() == "increase":
                current_roll = min(current_roll + 1, 6)  # Ensure it doesn't exceed 6
                luck -= 1
            elif modify_type and modify_type.lower() == "decrease":
                current_roll = max(current_roll - 1, 1)  # Ensure it doesn't go below 1
                luck -= 1
    return current_roll


def roll_dice():
    global luck
    dice_result = roll_two_dice()
    current_roll = dice_result[0]

    current_roll = apply_luck_modifier(current_roll)  # Allow luck modification

    # Update the count of the current roll
    roll_counts[current_roll] += 1

    # Check if the rolled number is the player's favorite number
    if current_roll == favorite_number:
        luck += 1  # Increment luck if favorite number is rolled

    # Get the current occurrence of this roll number
    occurrence = roll_counts[current_roll]

    # Fetch the prompt based on the current roll and its occurrence count
    current_prompt = journal_prompts.get(
        (current_roll, occurrence), "You've exhausted the prompts for this number."
    )

    prompt_label.config(
        text=f"Your roll: {current_roll} - {current_prompt}. Your luck: {luck}"
    )


def start_game():
    set_game_data()
    prompt_label.config(text="Describe your character: ")
    killerDescription.set(
        f"Killer wears a {game_data['killer']['mask']} with a {game_data['killer']['weapon']} and you remember this... {game_data['killer']['trait']}"
    )


# === UI ===
root = Tk()
root.title("One Page Left - Text Based RPG")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

main_interface = ttk.Frame(root, padding=(3, 3, 12, 12))
main_interface.grid(
    column=0,
    row=0,
)
main_interface.columnconfigure(0, weight=1)
main_interface.rowconfigure(0, weight=1)

prompt_label = ttk.Label(
    main_interface, text="Click start to begin the game.", wraplength=300
)
prompt_label.grid(column=0, row=1, sticky=("n", "s", "e", "w"))

button_frame = ttk.Frame(main_interface)
button_frame.grid(column=0, row=2)
dice_button = ttk.Button(button_frame, text="Roll Dice", command=roll_dice)
dice_button.grid(column=1, row=0)

start_button = ttk.Button(button_frame, text="Start Game", command=start_game)
start_button.grid(column=2, row=0)

input_frame = ttk.Frame(main_interface)
journal_entry = ttk.Entry(input_frame, width=68)
journal_entry.pack(side=LEFT)
submit_button = ttk.Button(input_frame, text="Submit", command=submit_entry)
submit_button.pack(side=LEFT)
input_frame.grid(column=0, row=3)

journal = Text(main_interface, height=20, width=75, wrap=WORD, state=DISABLED)
journal.grid(column=0, row=4)

killerDescription = StringVar()  # e = ttk.Entry(parent, textvariable=name)
killer_description = ttk.Label(
    root,
    text="",
    textvariable=killerDescription,
    wraplength=300,
    foreground="red",
    background="black",
    relief="sunken",
)
killer_description.grid(column=0, row=5)

root.mainloop()


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
