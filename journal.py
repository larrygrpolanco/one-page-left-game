import random
import tkinter.simpledialog as simpledialog
from tkinter import *
from tkinter import ttk
from rules import (
    character_archetypes,
    character_secrets,
    killer_masks,
    killer_weapons,
    killer_traits,
    journal_prompts,
)

# === Game Design ===
# Define game mechanics and UI layout

# === Initialize variables ===
roll_counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
luck = 1
favorite_number = 3
game_data = {
    "character": {"archetype": None, "secret": None},
    "killer": {"mask": None, "weapon": None, "trait": None},
}
total_word_count = 0
max_words = 500


def set_game_data():
    for key, value in [
        ("archetype", character_archetypes),
        ("secret", character_secrets),
        ("mask", killer_masks),
        ("weapon", killer_weapons),
        ("trait", killer_traits),
    ]:
        roll1, roll2 = roll_two_dice()
        game_data["character" if key in ["archetype", "secret"] else "killer"][key] = (
            value[roll1][roll2]
        )


def roll_two_dice():
    return random.randint(1, 6), random.randint(1, 6)


def submit_entry():
    global total_word_count
    entry_text = journal_entry.get()
    word_count = len(entry_text.split())
    new_total = total_word_count + word_count
    if new_total <= max_words:
        update_journal(entry_text)
        total_word_count = new_total
        word_count_progress["value"] = total_word_count
        journal_entry.delete(0, "end")
    else:
        prompt_label.config(
            text="You cannot exceed 500 words. Please revise your entry."
        )


def update_journal(text):
    journal.config(state="normal")
    journal.insert("end", text + "\n")
    journal.config(state="disabled")
    journal.yview("end")


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
                current_roll = min(current_roll + 1, 6)
                luck -= 1
            elif modify_type and modify_type.lower() == "decrease":
                current_roll = max(current_roll - 1, 1)
                luck -= 1
    return current_roll


def roll_dice():
    global luck
    dice_result = roll_two_dice()
    current_roll = dice_result[0]

    current_roll = apply_luck_modifier(current_roll)

    roll_counts[current_roll] += 1

    if current_roll == favorite_number:
        luck += 1

    occurrence = roll_counts[current_roll]
    current_prompt = journal_prompts.get(
        (current_roll, occurrence), "You've exhausted the prompts for this number."
    )

    prompt_label.config(text=f"Your roll: {current_roll} - {current_prompt}.")
    luck_count_label.config(text=f"Luck Points: {luck}")


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

main_frame = ttk.Frame(root, padding="3 3 12 12")
main_frame.grid(column=0, row=0, sticky=("n", "w", "e", "s"))
main_frame.columnconfigure(0, weight=1)
main_frame.rowconfigure(0, weight=1)
main_frame.rowconfigure(1, weight=1)
main_frame.rowconfigure(2, weight=1)
main_frame.rowconfigure(3, weight=1)
main_frame.rowconfigure(4, weight=1)
main_frame.rowconfigure(5, weight=1)

prompt_label = ttk.Label(
    main_frame, text="Click start to begin the game.", wraplength=300
)
prompt_label.grid(column=0, row=0, sticky=("n", "s", "e", "w"))

journal_entry = ttk.Entry(main_frame, width=50)
journal_entry.grid(column=0, row=2, sticky=("w", "e"))

submit_button = ttk.Button(main_frame, text="Submit", command=submit_entry)
submit_button.grid(column=1, row=2, sticky="w")

luck_count_label = ttk.Label(main_frame, text=f"Luck Points: {luck}")
luck_count_label.grid(column=1, row=3, sticky="w")

dice_button = ttk.Button(main_frame, text="Roll Dice", command=roll_dice)
dice_button.grid(column=1, row=4)

new_game_button = ttk.Button(main_frame, text="New Game", command=start_game)
new_game_button.grid(column=1, row=5)

word_count_progress = ttk.Progressbar(
    main_frame, orient="horizontal", length=200, mode="determinate", maximum=max_words
)
word_count_progress.grid(column=0, row=3, sticky=("w", "e"))

journal = Text(main_frame, height=10, width=50, state="disabled")
journal.grid(column=0, row=4, sticky=("w", "e"))

killerDescription = StringVar()
killer_description = ttk.Label(
    main_frame,
    text="",
    textvariable=killerDescription,
    wraplength=300,
    foreground="red",
    background="black",
    relief="sunken",
)
killer_description.grid(column=0, row=5, sticky=("n", "s", "e", "w"))

root.mainloop()

# Step 7: Integrate LLM for story generation
# Implement function to fetch story elements from LLM
# Handle and parse LLM responses and integrate them into the game

# === Testing and Iteration ===
# Step 8: Perform functional testing
# Test UI interactions
# Test dice rolling mechanics and journal updates

# Step 9: Perform gameplay testing
# Play the game to see how the mechanics and story unfold
# Adjust game logic and UI based on gameplay experience

# Step 10: Collect user feedback (if possible)
# Use feedback to refine game mechanics and UI

# === Finalization ===
# Step 11: Polish the UI
# Refine the UI based on test and user feedback

# Step 12: Write documentation
# Create simple documentation on how to install and play the game
