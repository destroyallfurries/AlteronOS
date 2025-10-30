#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk

class AlteronFileManager:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("AlterSearcher")
        self.window.geometry("600x400")
        self.setup_file_manager()
        
    def setup_file_manager(self):
        # Tree view for files
        self.tree = ttk.Treeview(self.window)
        self.tree.pack(fill=tk.BOTH, expand=True)
        
        # Add sample items
        self.tree.insert("", "end", text="System.dir", values=("Folder"))
        self.tree.insert("", "end", text="readme.txt", values=("Text File"))
        
    def run(self):
        self.window.mainloop()