import tkinter as tk
from tkinter import messagebox, font
import random

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Colorful Tic Tac Toe")
        self.root.geometry("500x600")
        self.root.configure(bg="#2c3e50")
        self.root.resizable(False, False)
        
        # Custom fonts
        self.title_font = font.Font(family="Helvetica", size=24, weight="bold")
        self.button_font = font.Font(family="Helvetica", size=16, weight="bold")
        self.status_font = font.Font(family="Helvetica", size=14)
        
        # Game variables
        self.current_player = "X"
        self.board = [" " for _ in range(9)]
        self.game_active = True
        self.x_score = 0
        self.o_score = 0
        
        # Colors
        self.colors = {
            "bg": "#2c3e50",
            "button_bg": "#34495e",
            "button_active": "#2c3e50",
            "button_fg": "#ecf0f1",
            "title": "#f1c40f",
            "x_color": "#e74c3c",
            "o_color": "#3498db",
            "status": "#ecf0f1",
            "reset_bg": "#e67e22",
            "reset_active": "#d35400"
        }
        
        self.create_widgets()
    
    def create_widgets(self):
        # Title
        self.title_label = tk.Label(
            self.root, 
            text="TIC TAC TOE", 
            font=self.title_font, 
            fg=self.colors["title"], 
            bg=self.colors["bg"]
        )
        self.title_label.pack(pady=(20, 10))
        
        # Score display
        self.score_frame = tk.Frame(self.root, bg=self.colors["bg"])
        self.score_frame.pack()
        
        self.x_score_label = tk.Label(
            self.score_frame, 
            text=f"Player X: {self.x_score}", 
            font=self.status_font, 
            fg=self.colors["x_color"], 
            bg=self.colors["bg"]
        )
        self.x_score_label.pack(side="left", padx=20)
        
        self.o_score_label = tk.Label(
            self.score_frame, 
            text=f"Player O: {self.o_score}", 
            font=self.status_font, 
            fg=self.colors["o_color"], 
            bg=self.colors["bg"]
        )
        self.o_score_label.pack(side="right", padx=20)
        
        # Status label
        self.status_label = tk.Label(
            self.root, 
            text=f"Player {self.current_player}'s turn", 
            font=self.status_font, 
            fg=self.colors["status"], 
            bg=self.colors["bg"]
        )
        self.status_label.pack(pady=10)
        
        # Game board
        self.board_frame = tk.Frame(self.root, bg=self.colors["bg"])
        self.board_frame.pack()
        
        self.buttons = []
        for i in range(9):
            row, col = divmod(i, 3)
            button = tk.Button(
                self.board_frame,
                text=" ", 
                font=self.button_font,
                width=6, 
                height=3,
                bg=self.colors["button_bg"],
                activebackground=self.colors["button_active"],
                fg=self.colors["button_fg"],
                relief="ridge",
                borderwidth=3,
                command=lambda idx=i: self.on_button_click(idx)
            )
            button.grid(row=row, column=col, padx=5, pady=5)
            self.buttons.append(button)
        
        # Reset button
        self.reset_button = tk.Button(
            self.root,
            text="Reset Game", 
            font=self.button_font,
            width=15,
            bg=self.colors["reset_bg"],
            activebackground=self.colors["reset_active"],
            fg=self.colors["button_fg"],
            relief="raised",
            borderwidth=3,
            command=self.reset_game
        )
        self.reset_button.pack(pady=20)
    
    def on_button_click(self, index):
        if self.board[index] == " " and self.game_active:
            self.board[index] = self.current_player
            self.update_button(index)
            
            if self.check_winner():
                self.handle_win()
            elif " " not in self.board:
                self.handle_draw()
            else:
                self.switch_player()
    
    def update_button(self, index):
        button = self.buttons[index]
        value = self.board[index]
        button.config(text=value, state="disabled")
        
        if value == "X":
            button.config(fg=self.colors["x_color"])
        else:
            button.config(fg=self.colors["o_color"])
    
    def check_winner(self):
        # Check rows, columns, and diagonals
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]              # diagonals
        ]
        
        for combo in winning_combinations:
            a, b, c = combo
            if self.board[a] == self.board[b] == self.board[c] != " ":
                # Highlight winning combination
                for idx in combo:
                    self.buttons[idx].config(bg="#27ae60")
                return True
        return False
    
    def handle_win(self):
        self.game_active = False
        winner = self.current_player
        self.status_label.config(text=f"Player {winner} wins!")
        
        # Update score
        if winner == "X":
            self.x_score += 1
            self.x_score_label.config(text=f"Player X: {self.x_score}")
        else:
            self.o_score += 1
            self.o_score_label.config(text=f"Player O: {self.o_score}")
        
        messagebox.showinfo("Game Over", f"Player {winner} wins!")
    
    def handle_draw(self):
        self.game_active = False
        self.status_label.config(text="Game ended in a draw!")
        messagebox.showinfo("Game Over", "It's a draw!")
    
    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"
        self.status_label.config(text=f"Player {self.current_player}'s turn")
    
    def reset_game(self):
        self.current_player = "X"
        self.board = [" " for _ in range(9)]
        self.game_active = True
        
        for button in self.buttons:
            button.config(
                text=" ", 
                state="normal", 
                bg=self.colors["button_bg"],
                fg=self.colors["button_fg"]
            )
        
        self.status_label.config(text=f"Player {self.current_player}'s turn")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
