import tkinter as tk
from tkinter import messagebox
import math

# Initialize the window
window = tk.Tk()
window.title("Tic Tac Toe - You vs AI")
window.resizable(False, False)

# Initial board
board = [" " for _ in range(9)]
buttons = []

# Check for win
def check_winner(brd, player):
    win_combos = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for combo in win_combos:
        if all(brd[i] == player for i in combo):
            return True
    return False

# Check for draw
def is_draw(brd):
    return " " not in brd

# Minimax function
def minimax(brd, depth, is_maximizing):
    if check_winner(brd, "O"):
        return 1
    elif check_winner(brd, "X"):
        return -1
    elif is_draw(brd):
        return 0

    if is_maximizing:
        best = -math.inf
        for i in range(9):
            if brd[i] == " ":
                brd[i] = "O"
                score = minimax(brd, depth + 1, False)
                brd[i] = " "
                best = max(best, score)
        return best
    else:
        best = math.inf
        for i in range(9):
            if brd[i] == " ":
                brd[i] = "X"
                score = minimax(brd, depth + 1, True)
                brd[i] = " "
                best = min(best, score)
        return best

# AI move using Minimax
def ai_move():
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    if move is not None:
        board[move] = "O"
        buttons[move]["text"] = "O"
        buttons[move]["state"] = "disabled"
        check_game_over()

# Handle button click
def on_click(i):
    if board[i] == " ":
        board[i] = "X"
        buttons[i]["text"] = "X"
        buttons[i]["state"] = "disabled"
        if not check_game_over():
            window.after(500, ai_move)

# Check if game over
def check_game_over():
    if check_winner(board, "X"):
        messagebox.showinfo("Game Over","You Win!")
        disable_all_buttons()
        return True
    elif check_winner(board, "O"):
        messagebox.showinfo("Game Over","AI Wins!")
        disable_all_buttons()
        return True
    elif is_draw(board):
        messagebox.showinfo("Game Over", "It's a Draw!")
        disable_all_buttons()
        return True
    return False

# Disable all buttons
def disable_all_buttons():
    for b in buttons:
        b["state"] = "disabled"

# Restart the game
def restart():
    global board
    board = [" " for _ in range(9)]
    for i in range(9):
        buttons[i]["text"] = " "
        buttons[i]["state"] = "normal"

# Create grid of buttons
frame = tk.Frame(window)
frame.pack()

for i in range(9):
    b = tk.Button(frame, text=" ", width=6, height=3, font=("Times new roman", 24), command=lambda i=i: on_click(i))
    b.grid(row=i//3, column=i%3)
    buttons.append(b)

# Restart button
restart_btn = tk.Button(window, text="Restart", font=("Times new roman", 18), command=restart)
restart_btn.pack(pady=10)

# Run the app
window.mainloop()