#!/usr/bin/env python3
import tkinter as tk
from terminals import TerminalManager

class MultiTerminalGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("AlteronOS Multi-Terminal")
        self.window.geometry("800x600")
        self.terminal_mgr = TerminalManager()
        self.setup_gui()
        
    def setup_gui(self):
        # Terminal selection
        self.terminal_var = tk.StringVar()
        terminal_combo = tk.OptionMenu(self.window, self.terminal_var, *self.terminal_mgr.terminals.keys())
        terminal_combo.pack()
        
        # Terminal output
        self.output_text = tk.Text(self.window)
        self.output_text.pack(fill=tk.BOTH, expand=True)
        
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    gui = MultiTerminalGUI()
    gui.run()