#!/usr/bin/env python3
import tkinter as tk

class AlteronLogin:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("AlteronOS Login")
        self.root.geometry("400x300")
        self.setup_login()
        
    def setup_login(self):
        tk.Label(self.root, text="Username:").pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()
        
        tk.Label(self.root, text="Password:").pack()
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack()
        
        tk.Button(self.root, text="Login", command=self.login).pack()
        
    def login(self):
        username = self.username_entry.get()
        print(f"Login: {username}")
        self.root.destroy()
        from desktop import AlteronDesktop
        desktop = AlteronDesktop()
        desktop.run()
        
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    login = AlteronLogin()
    login.run()