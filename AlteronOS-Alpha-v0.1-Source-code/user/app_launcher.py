#!/usr/bin/env python3
import tkinter as tk
from compatibility import UniversalCompatibility

class UniversalAppLauncher:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("App Launcher")
        self.window.geometry("500x400")
        self.compat = UniversalCompatibility()
        self.setup_launcher()
        
    def setup_launcher(self):
        tk.Label(self.window, text="Supported formats: .exe, .deb, .dmg, .txt").pack()
        tk.Button(self.window, text="Launch App", command=self.launch_app).pack()
        
    def launch_app(self):
        print("Launching app...")
        
    def run(self):
        self.window.mainloop()