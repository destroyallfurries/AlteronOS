#!/usr/bin/env python3
class BaseTerminal:
    def __init__(self, name):
        self.name = name
        
    def execute(self, command):
        return f"{self.name}: {command}"

class RustTerminal(BaseTerminal):
    def __init__(self):
        super().__init__("Rust Terminal")
        
class GoTerminal(BaseTerminal):
    def __init__(self):
        super().__init__("Go Terminal")
        
class LinuxTerminal(BaseTerminal):
    def __init__(self):
        super().__init__("Linux Terminal")

class TerminalManager:
    def __init__(self):
        self.terminals = {
            'rust': RustTerminal(),
            'go': GoTerminal(),
            'linux': LinuxTerminal()
        }