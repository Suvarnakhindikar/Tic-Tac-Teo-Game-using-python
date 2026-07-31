import tkinter as tk
from tkinter import messagebox

# Create main window
root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("370x380")

# Current player
current_player = "X"

# Store buttons
buttons = []


# Function to check winner
def check_winner():
    win_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in win_combinations:
        if buttons[a]["text"] == buttons[b]["text"] == buttons[c]["text"] != "":
            return True

    return False


# Function to check draw
def check_draw():
    for button in buttons:
        if button["text"] == "":
            return False
    return True


# Button click function
def button_click(index):
    global current_player

    if buttons[index]["text"] == "":
        buttons[index]["text"] = current_player

        if check_winner():
            messagebox.showinfo("Winner", f"Player {current_player} Wins!")
            disable_buttons()
            return

        if check_draw():
            messagebox.showinfo("Draw", "Game Draw!")
            return

        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"


# Disable all buttons
def disable_buttons():
    for button in buttons:
        button.config(state="disabled")


# Restart game
def restart_game():
    global current_player
    current_player = "X"

    for button in buttons:
        button.config(text="", state="normal")


# Create 9 buttons
for i in range(9):
    btn = tk.Button(
        root,
        text="",
        font=("Arial", 24),
        width=5,
        height=2,
        command=lambda i=i: button_click(i)
    )

    btn.grid(row=i // 3, column=i % 3)
    buttons.append(btn)


# Restart button
restart = tk.Button(
    root,
    text="Restart",
    font=("Arial", 14),
    command=restart_game
)
restart.grid(row=3, column=0, columnspan=3, sticky="nsew", pady=4, padx=15)

# Start application
root.mainloop()