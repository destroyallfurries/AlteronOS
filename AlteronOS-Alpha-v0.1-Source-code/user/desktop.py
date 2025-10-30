#!/usr/bin/env python3
import tkinter as tk

class AlteronDesktop:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("AlteronOS Desktop")
        self.root.geometry("1024x768")
        self.setup_desktop()
        
    def setup_desktop(self):
        # Taskbar
        taskbar = tk.Frame(self.root, bg="gray", height=40)
        taskbar.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Start button
        start_btn = tk.Button(taskbar, text="Alteron", command=self.show_start_menu)
        start_btn.pack(side=tk.LEFT)
        
        # Desktop icons
        desktop_frame = tk.Frame(self.root)
        desktop_frame.pack(fill=tk.BOTH, expand=True)
        
        icons = [
            ("File Manager", self.open_file_manager),
            ("Terminal", self.open_terminal),
            ("Settings", self.open_settings)
        ]
        
        for name, command in icons:
            btn = tk.Button(desktop_frame, text=name, command=command)
            btn.pack(side=tk.LEFT, padx=10, pady=10)
            
    def show_start_menu(self):
        print("Start menu")
        
    def open_file_manager(self):
        from file_manager import AlteronFileManager
        file_mgr = AlteronFileManager(self.root)
        
    def open_terminal(self):
        from terminal_gui import MultiTerminalGUI
        terminal = MultiTerminalGUI()
        
    def open_settings(self):
        print("Settings")
        
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    desktop = AlteronDesktop()
    desktop.run()