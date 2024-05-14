import random
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QLabel, QLineEdit, QPushButton,
    QTextEdit, QProgressBar, QDialog, QDialogButtonBox, QFormLayout, QInputDialog
)
from PyQt5.QtCore import Qt, QTimer, QEventLoop
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

class GameWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.setWindowTitle("One Page Left - Text Based RPG")

    def initUI(self):
        self.main_layout = QVBoxLayout()

        self.prompt_label = QLabel("Click start to begin the game.")
        self.prompt_label.setWordWrap(True)
        self.main_layout.addWidget(self.prompt_label)

        self.journal_entry = QLineEdit()
        self.main_layout.addWidget(self.journal_entry)

        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.submit_entry)
        self.main_layout.addWidget(self.submit_button)

        self.luck_count_label = QLabel(f"Luck Points: {luck}")
        self.main_layout.addWidget(self.luck_count_label)

        self.dice_button = QPushButton("Roll Dice")
        self.dice_button.clicked.connect(self.roll_dice)
        self.main_layout.addWidget(self.dice_button)

        self.new_game_button = QPushButton("New Game")
        self.new_game_button.clicked.connect(self.start_game)
        self.main_layout.addWidget(self.new_game_button)

        self.word_count_progress = QProgressBar()
        self.word_count_progress.setMaximum(max_words)
        self.main_layout.addWidget(self.word_count_progress)

        self.journal = QTextEdit()
        self.journal.setReadOnly(True)
        self.main_layout.addWidget(self.journal)

        self.killerDescription = QLabel("")
        self.killerDescription.setWordWrap(True)
        self.killerDescription.setStyleSheet("color: red; background-color: black;")
        self.main_layout.addWidget(self.killerDescription)

        central_widget = QMainWindow()
        central_widget.setLayout(self.main_layout)
        self.setCentralWidget(central_widget)

    def submit_entry(self):
        global total_word_count
        entry_text = self.journal_entry.text()
        word_count = len(entry_text.split())
        new_total = total_word_count + word_count
        if new_total <= max_words:
            self.update_journal(entry_text)
            total_word_count = new_total
            self.word_count_progress.setValue(total_word_count)
            self.journal_entry.clear()
        else:
            self.prompt_label.setText("You cannot exceed 500 words. Please revise your entry.")

    def update_journal(self, text):
        self.journal.append(text)

    def apply_luck_modifier(self, current_roll):
        global luck
        if luck > 0:
            modify, ok = QInputDialog.getText(self, "Modify Roll", "Do you want to use 1 luck point to modify your roll? (y/n):")
            if ok and modify.lower() == "y":
                modify_type, ok = QInputDialog.getText(self, "Increase or Decrease", "Type 'increase' to add 1 or 'decrease' to subtract 1:")
                if ok and modify_type.lower() == "increase":
                    current_roll = min(current_roll + 1, 6)
                    luck -= 1
                elif ok and modify_type.lower() == "decrease":
                    current_roll = max(current_roll - 1, 1)
                    luck -= 1
        return current_roll

    def roll_dice(self):
        global luck
        dice_result = roll_two_dice()
        current_roll = dice_result[0]

        current_roll = self.apply_luck_modifier(current_roll)

        roll_counts[current_roll] += 1

        if current_roll == favorite_number:
            luck += 1

        occurrence = roll_counts[current_roll]
        current_prompt = journal_prompts.get(
            (current_roll, occurrence), "You've exhausted the prompts for this number."
        )

        self.prompt_label.setText(f"Your roll: {current_roll} - {current_prompt}.")
        self.luck_count_label.setText(f"Luck Points: {luck}")

    def start_game(self):
        set_game_data()
        self.prompt_label.setText("Describe your character: ")
        self.killerDescription.setText(
            f"Killer wears a {game_data['killer']['mask']} with a {game_data['killer']['weapon']} and you remember this... {game_data['killer']['trait']}"
        )

if __name__ == "__main__":
    app = QApplication([])
    window = GameWindow()
    window.show()
    app.exec_()


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
