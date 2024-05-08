# === Game Design ===
# Step 3: Understand and define game mechanics
# - Clearly define how dice rolls, character creation, journaling, and end-game conditions work

# Step 4: Design the UI layout
# - Sketch out a preliminary design of the UI, focusing on usability and game flow


# === Character and killer creation ====
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
character_secrets = {
    1: {
        1: "You’re not who you claim to be",
        2: "You lost your dream job",
        3: "You just lost your partner/spouse",
        4: "You are taking care of a child",
        5: "You recently retired / quit your crappy job",
        6: "You have a physical disability",
    },
    2: {
        1: "You were recently released from a mental facility",
        2: "You recently escaped police custody",
        3: "You are obsessed with horror movies",
        4: "You bullied someone so bad they nearly died",
        5: "You ran away from home",
        6: "You are camping out in the wilderness",
    },
    3: {
        1: "You recenly won the lottery",
        2: "You recently got out of rehab",
        3: "Someone you love recently went missing",
        4: "You got a letter from your biological parents",
        5: "You got a weird call from your ex",
        6: "You recently got out of an abusive relationship",
    },
    4: {
        1: "You recently inherited the family fortune",
        2: "You have been having visions of your own death",
        3: "When you were young you used to talk to ghosts",
        4: "You are obssessed with conspiracy theories",
        5: "You inherited a strange artifact/item",
        6: "Your blog/channel recently blew up",
    },
    5: {
        1: "You are a criminal informant",
        2: "There's something only you can fix",
        3: "Your loved one is in the hospital right now",
        4: "Your spouse is going into childbirth",
        5: "You witnessed a murder when you were young",
        6: "You just got laid with your dream person",
    },
    6: {
        1: "You're looking for a new start in a new city",
        2: "You found a weird book in the local library",
        3: "Your art has been torturing you…",
        4: "You are part of an affair",
        5: "You've been invited to the party of",
        6: "You are blackmailing someone",
    },
}
killer_masks = {
    1: {
        1: "Alien Mask",
        2: "Animal Head",
        3: "Anime Mask",
        4: "Sun Glasses",
        5: "Ski Mask",
        6: "Bandages",
    },
    2: {
        1: "Big Hat",
        2: "Biker Helmet",
        3: "Burlap Sack",
        4: "Cardboard Mask",
        5: "Carnival Mask",
        6: "Cartoon Character",
    },
    3: {
        1: "Celebrity Mask",
        2: "Clown Mask/Makeup",
        3: "Devil Mask",
        4: "Dinosaur Mask",
        5: "Doll Mask",
        6: "Eyepatch",
    },
    4: {
        1: "Gas Mask",
        2: "Guy Fawkes Mask",
        3: "Hockey Mask",
        4: "Human Flesh",
        5: "Jack O’Lantern",
        6: "Mascot Head",
    },
    5: {
        1: "Masquerade Mask",
        2: "Pantyhose",
        3: "Paper Bag",
        4: "Paper Plate",
        5: "Plague Doctor",
        6: "Skull / Skeleton",
    },
    6: {
        1: "Surgical Mask",
        2: "Theater Mask",
        3: "TV / Monitor",
        4: "VR Headset",
        5: "Veil / Wedding Veil",
        6: "Welded Metal Mask",
    },
}
killer_weapons = {
    1: {
        1: "Axe",
        2: "Baseball Bat",
        3: "Bow & Arrow",
        4: "Buzz Saw",
        5: "Cane",
        6: "Chainsaw",
    },
    2: {
        1: "Claws",
        2: "Cleaver",
        3: "Crowbar",
        4: "Folding Chair",
        5: "Garrote/Piano Wire",
        6: "Giant Scissors",
    },
    3: {
        1: "Guitar",
        2: "Hacksaw",
        3: "Hammer",
        4: "Hockey Stick",
        5: "Hook & Chain",
        6: "Ice Pick",
    },
    4: {
        1: "Katana",
        2: "Knife",
        3: "Lead Pipe",
        4: "Machete",
        5: "Musket",
        6: "Nail Gun",
    },
    5: {
        1: "Pickaxe",
        2: "Pitchfork",
        3: "Revolver",
        4: "Rope & Noose",
        5: "Scalpel",
        6: "Screwdriver",
    },
    6: {
        1: "Scythe",
        2: "Shank",
        3: "Shovel",
        4: "Spear",
        5: "Straight Razor",
        6: "Welding Torch",
    },
}
killer_traits = {
    1: {
        1: "Behaves Robotically",
        2: "Broken Shackles",
        3: "Burnt Skin",
        4: "Constantly Crying",
        5: "Constantly Laughing",
        6: "Covered in Mold",
    },
    2: {
        1: "Covered in Scars",
        2: "Covered in Tattoos",
        3: "Cultish Robes",
        4: "Clockwork Noises",
        5: "Emits Coldness",
        6: "Emits Fog",
    },
    3: {
        1: "Extra Limbs",
        2: "Extra Long Fingers",
        3: "Has Gills",
        4: "Glowing Brand",
        5: "Glowing Eyes",
        6: "Has No Shadow",
    },
    4: {
        1: "Horns",
        2: "Hot as Hell",
        3: "Long Neck",
        4: "Metallic Voice",
        5: "Music Follows Them",
        6: "Only Seen in Mirrors",
    },
    5: {
        1: "Prosthetics",
        2: "Huge Muscles",
        3: "Rotting Flesh",
        4: "Silent Footsteps",
        5: "Speaks like a Child",
        6: "Surrounded by Static",
    },
    6: {
        1: "Tall and Slender",
        2: "Tantalizing Voice",
        3: "Very Long Hair",
        4: "Walks on all Fours",
        5: "Wedding Dress",
        6: "Wide Frame",
    },
}


# Function to get the character archetype based on dice rolls
def roll_two_dice():
    return random.randint(1, 6), random.randint(1, 6)


def set_game_data():
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


# Dictionary to hold game data like a JSON object
game_data = {
    "character": {"archetype": None, "secret": None},
    "killer": {"mask": None, "weapon": None, "trait": None},
}


# Function to update journal text
def update_journal(text):
    journal.config(state=tk.NORMAL)  # Enable text widget for editing
    journal.insert(tk.END, text + "\n")  # Append text
    journal.config(state=tk.DISABLED)  # Disable text widget to prevent user editing
    journal.yview(tk.END)  # Auto-scroll to the end


# Function to initiate game and handle user inputs
def start_game():
    set_game_data()
    update_journal(
        "You are a"
        + game_data["character"]["archetype"]
        + " and "
        + game_data["character"]["secret"]
    )
    update_journal(
        "Introduce your character the same way you would do in a diary. Describe yourself and your problems but don’t linger…"
    )

    update_journal("Killer's Mask: " + game_data["killer"]["mask"])
    update_journal("Killer's Weapon: " + game_data["killer"]["weapon"])
    update_journal("Killer's Trait: " + game_data["killer"]["trait"])

    input_frame.pack()  # Show input options to the user


def submit_entry():
    entry_text = journal_entry.get()
    update_journal(entry_text)
    journal_entry.delete(0, tk.END)  # Clear input field
    # Continue with next parts of the game...


# === Game Logic ===
import random


# - Dice roll functionality
def roll_dice():
    return random.randint(1, 6)


# - Game progression logic based on the rules


# === UI ===
# Implement the basic UI setup
import tkinter as tk

# Setup tkinter window
root = tk.Tk()
root.title("One Page Left - Text Based RPG")

# Create a scrolled text widget for the journal
journal = tk.Text(root, height=40, width=75, wrap=tk.WORD)
journal.pack(padx=10, pady=10)
journal.config(state=tk.DISABLED)  # Start with the text widget disabled for editing

# Frame for user inputs
input_frame = tk.Frame(root)
journal_entry = tk.Entry(input_frame, width=68)
journal_entry.pack(side=tk.LEFT)
submit_button = tk.Button(input_frame, text="Submit", command=submit_entry)
submit_button.pack(side=tk.LEFT)

# Start the game by setting initial journal entry
start_button = tk.Button(root, text="Start Game", command=start_game)
start_button.pack(pady=10)


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
