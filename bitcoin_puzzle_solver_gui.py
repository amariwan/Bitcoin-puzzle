import tkinter as tk
from tkinter import messagebox
import threading
from bitcoin_puzzle_solver import BitcoinPuzzleSolver

class BitcoinPuzzleGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Bitcoin Puzzle Solver")

        tk.Label(root, text="Minimum Key:").grid(row=0, column=0)
        self.min_key_entry = tk.Entry(root)
        self.min_key_entry.grid(row=0, column=1)

        tk.Label(root, text="Maximum Key:").grid(row=1, column=0)
        self.max_key_entry = tk.Entry(root)
        self.max_key_entry.grid(row=1, column=1)

        tk.Label(root, text="Target Wallet:").grid(row=2, column=0)
        self.wallet_entry = tk.Entry(root)
        self.wallet_entry.grid(row=2, column=1)

        tk.Label(root, text="Chunks:").grid(row=3, column=0)
        self.chunks_entry = tk.Entry(root)
        self.chunks_entry.grid(row=3, column=1)

        self.start_button = tk.Button(root, text="Start", command=self.start_solver)
        self.start_button.grid(row=4, column=0, columnspan=2)

        self.status_label = tk.Label(root, text="Status: Ready")
        self.status_label.grid(row=5, column=0, columnspan=2)

    def start_solver(self):
        min_key = int(self.min_key_entry.get())
        max_key = int(self.max_key_entry.get())
        wallet = self.wallet_entry.get()
        chunks = int(self.chunks_entry.get())

        self.status_label.config(text="Status: Solving...")
        threading.Thread(target=self.solve_puzzle, args=(min_key, max_key, wallet, chunks)).start()

    def solve_puzzle(self, min_key, max_key, wallet, chunks):
        solver = BitcoinPuzzleSolver(min_key, max_key, wallet, chunks)
        found_key = solver.solve()

        if found_key:
            messagebox.showinfo("Result", f"Key found: {found_key}")
        else:
            messagebox.showinfo("Result", "No key found within the given range.")

        self.status_label.config(text="Status: Ready")

if __name__ == "__main__":
    root = tk.Tk()
    app = BitcoinPuzzleGUI(root)
    root.mainloop()
