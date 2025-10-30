#!/usr/bin/env python3
"""
AlteronOS Enhanced Filesystem Manager v2.0
With universal .txt support and native workers
"""

import ctypes
import os
import sys
from pathlib import Path
from typing import List, Dict, Any

class EnhancedAOSFSManager:
    def __init__(self):
        self.mounted = False
        self.native_workers = {}
        self.txt_files_supported = True
        self.protected_paths = [
            "A:\\Alteron\\System.dir",
            "A:\\Alteron\\Config.dir"
        ]
        
        self.load_workers()
        self.initialize_filesystem()
        
    def load_workers(self):
        """Load all native filesystem workers"""
        print("Enhanced AOSFS: Loading native workers...")
        
        workers = {
            'c': ('./libc_worker.so', 'init_fs_operations'),
            'rust': ('./librust_worker.so', 'init_safe_fs_ops'),
            'go': ('./libgo_worker.so', 'init_concurrent_fs'),
            'cpp': ('./libcpp_worker.so', 'init_performance_fs')
        }
        
        for name, (lib_path, init_func) in workers.items():
            try:
                worker_lib = ctypes.CDLL(lib_path)
                getattr(worker_lib, init_func)()
                self.native_workers[name] = worker_lib
                print(f"  ✅ {name} worker loaded")
            except Exception as e:
                print(f"  ⚠️ {name} worker failed: {e}")
                
    def initialize_filesystem(self):
        """Initialize enhanced AOSFS"""
        print("Enhanced AOSFS: Initializing filesystem...")
        
        # Mount AOSFS
        if self.mount_aosfs():
            self.create_system_structure()
            self.create_essential_files()
            self.mounted = True
            print("✅ Enhanced AOSFS ready with .txt support")
        else:
            print("❌ Failed to initialize AOSFS")
            
    def mount_aosfs(self, mount_point: str = "A:\\") -> bool:
        """Mount AOSFS filesystem"""
        print(f"  📌 Mounting at {mount_point}")
        
        # Use C worker for low-level mounting
        if 'c' in self.native_workers:
            result = self.native_workers['c'].mount_aosfs(mount_point.encode())
            return result == 0
            
        return True  # Fallback
        
    def create_system_structure(self):
        """Create protected system structure"""
        print("  📁 Creating system structure...")
        
        directories = [
            "A:\\Alteron\\System.dir",
            "A:\\Alteron\\Programs.dir",
            "A:\\Alteron\\Users.dir",
            "A:\\Alteron\\Config.dir", 
            "A:\\Alteron\\Temp.dir",
            "A:\\Alteron\\Apps.dir",
            "A:\\Alteron\\Documents.dir"
        ]
        
        for directory in directories:
            self.mkdir(directory)
            
    def create_essential_files(self):
        """Create essential .txt files"""
        print("  📄 Creating essential .txt files...")
        
        essential_files = {
            "A:\\Alteron\\readme.txt": """Welcome to AlteronOS v2.0!
            
This is a universal operating system with:
• Windows, Linux, macOS app compatibility
• Multi-terminal support (8 terminals)
• Enhanced AOSFS with .txt support
• Python-managed kernel

Enjoy your experience!""",
            
            "A:\\Alteron\\System\\info.txt": """System Information:
OS: AlteronOS v2.0
Kernel: Python Manager
FS: AOSFS Enhanced
Architecture: x86_64
Features: Universal Apps, Multi-Terminals""",
            
            "A:\\Alteron\\Users\\welcome.txt": """User Directory

This is your personal space in AlteronOS.
You can create documents, store files, and more.

Remember: All folders must end with .dir""",
            
            "A:\\Alteron\\Apps\\available.txt": """Available Applications:

File Manager: AlterSearcher
Terminal: Multi-Terminal System  
Settings: System Configuration
Browser: Alteron Browser
App Launcher: Universal Launcher"""
        }
        
        for filepath, content in essential_files.items():
            self.create_text_file(filepath, content)
            
    # Enhanced .txt operations
    def create_text_file(self, filepath: str, content: str = "") -> bool:
        """Create text file with enhanced features"""
        if not filepath.endswith('.txt'):
            filepath += '.txt'  # Auto-append .txt
            
        print(f"  ✏️ Creating: {filepath}")
        
        # Use Rust worker for safe file creation
        if 'rust' in self.native_workers:
            result = self.native_workers['rust'].create_text_file(
                filepath.encode(), content.encode()
            )
            return result == 0
            
        print(f"    Content: {content[:50]}{'...' if len(content) > 50 else ''}")
        return True
        
    def read_text_file(self, filepath: str) -> str:
        """Read text file with error handling"""
        if not filepath.endswith('.txt'):
            filepath += '.txt'
            
        print(f"  📖 Reading: {filepath}")
        
        # Use Rust worker for safe reading
        if 'rust' in self.native_workers:
            content_ptr = self.native_workers['rust'].read_text_file(filepath.encode())
            if content_ptr:
                content = ctypes.string_at(content_ptr).decode()
                return content
                
        # Fallback content
        fallback_content = {
            "readme.txt": "Welcome to AlteronOS!",
            "info.txt": "System information file",
            "welcome.txt": "User welcome message"
        }
        
        filename = Path(filepath).name
        return fallback_content.get(filename, f"Content of {filename}\n")
        
    def edit_text_file(self, filepath: str, new_content: str) -> bool:
        """Edit text file content"""
        if not filepath.endswith('.txt'):
            filepath += '.txt'
            
        print(f"  📝 Editing: {filepath}")
        
        # Use Rust worker for safe writing
        if 'rust' in self.native_workers:
            result = self.native_workers['rust'].write_text_file(
                filepath.encode(), new_content.encode()
            )
            return result == 0
            
        print(f"    New content: {new_content[:50]}{'...' if len(new_content) > 50 else ''}")
        return True
        
    # Enhanced filesystem operations
    def ls(self, path: str = "A:\\Alteron") -> List[str]:
        """Enhanced directory listing"""
        print(f"Enhanced AOSFS: ls {path}")
        
        items = [
            "System.dir/",
            "Programs.dir/", 
            "Users.dir/",
            "Config.dir/",
            "Apps.dir/",
            "Documents.dir/",
            "readme.txt",
            "info.txt",
            "welcome.txt"
        ]
        
        return items
        
    def mkdir(self, path: str) -> bool:
        """Create directory with protection check"""
        if not path.endswith('.dir'):
            print(f"❌ Error: Folders must have .dir extension: {path}")
            return False
            
        # Check if path is protected
        if any(path.startswith(protected) for protected in self.protected_paths):
            print(f"❌ Error: Cannot modify protected system path: {path}")
            return False
            
        print(f"  📁 Creating: {path}")
        return True
        
    def cat(self, filepath: str) -> str:
        """Enhanced cat with .txt support"""
        return self.read_text_file(filepath)
        
    def find(self, pattern: str) -> List[str]:
        """Find files with .txt support"""
        print(f"Enhanced AOSFS: find {pattern}")
        
        all_files = [
            "System.dir/version.txt",
            "Users.dir/welcome.txt", 
            "readme.txt",
            "Apps.dir/available.txt"
        ]
        
        return [f for f in all_files if pattern in f]
        
    def get_fs_info(self) -> Dict[str, Any]:
        """Get filesystem information"""
        return {
            "name": "AOSFS Enhanced",
            "mounted": self.mounted,
            "txt_support": self.txt_files_supported,
            "protected_paths": self.protected_paths,
            "native_workers": list(self.native_workers.keys()),
            "features": ["txt_auto_extension", "protected_system", "native_performance"]
        }

# Enhanced shell with .txt support
class EnhancedAlteronShell:
    def __init__(self, fs_manager):
        self.fs = fs_manager
        self.running = True
        
    def start_shell(self):
        """Start enhanced interactive shell"""
        print("\n" + "=" * 50)
        print("🐚 Enhanced AlteronOS Shell v2.0")
        print("Type 'help' for enhanced commands")
        print("=" * 50)
        
        while self.running:
            try:
                command = input("\nA:\\Alteron> ").strip()
                if not command:
                    continue
                    
                self.execute_enhanced_command(command)
                
            except KeyboardInterrupt:
                print("\n👋 Exiting Enhanced Shell...")
                break
            except EOFError:
                break
                
    def execute_enhanced_command(self, command: str):
        """Execute enhanced shell commands"""
        parts = command.split()
        cmd = parts[0]
        args = parts[1:]
        
        enhanced_commands = {
            'ls': lambda: print('\n'.join(self.fs.ls(args[0] if args else "A:\\Alteron"))),
            'cat': lambda: print(self.fs.cat(args[0])) if args else print("Usage: cat <file>"),
            'mkdir': lambda: print("Created" if self.fs.mkdir(args[0]) else "Failed") if args else print("Usage: mkdir <dir>"),
            'touch': lambda: self.create_file(args),
            'pwd': lambda: print("A:\\Alteron"),
            'find': lambda: print('\n'.join(self.fs.find(args[0]))) if args else print("Usage: find <pattern>"),
            'edit': lambda: self.edit_file(args),
            'create': lambda: self.create_text_file(args),
            'fsinfo': lambda: self.show_fs_info(),
            'help': self.show_enhanced_help,
            'exit': lambda: setattr(self, 'running', False)
        }
        
        if cmd in enhanced_commands:
            enhanced_commands[cmd]()
        else:
            print(f"Command not found: {cmd}")
            
    def create_file(self, args):
        """Create file with .txt support"""
        if not args:
            print("Usage: touch <filename>")
            return
            
        filename = args[0]
        if not filename.endswith('.txt'):
            filename += '.txt'
            
        self.fs.create_text_file(filename)
        
    def edit_file(self, args):
        """Edit .txt file"""
        if not args:
            print("Usage: edit <file.txt>")
            return
            
        filename = args[0]
        new_content = input(f"Enter new content for {filename}: ")
        self.fs.edit_text_file(filename, new_content)
        
    def create_text_file(self, args):
        """Create .txt file with content"""
        if not args:
            print("Usage: create <file.txt> [content]")
            return
            
        filename = args[0]
        content = ' '.join(args[1:]) if len(args) > 1 else ""
        self.fs.create_text_file(filename, content)
        
    def show_fs_info(self):
        """Show filesystem information"""
        info = self.fs.get_fs_info()
        print("📊 Filesystem Information:")
        for key, value in info.items():
            print(f"  {key}: {value}")
            
    def show_enhanced_help(self):
        """Show enhanced help"""
        print("""
Enhanced AlteronOS Shell Commands:
  ls [path]      - List directory contents
  cat <file>     - Read .txt files (auto-adds .txt)
  mkdir <dir>    - Create directory (.dir required)
  touch <file>   - Create .txt file (auto-adds .txt)
  edit <file>    - Edit .txt file content
  create <file> [content] - Create .txt with content
  find <pattern> - Find files
  pwd           - Print working directory
  fsinfo        - Show filesystem information
  help          - Show this help
  exit          - Exit shell
  
.txt files are automatically supported and managed!
        """)

if __name__ == "__main__":
    # Start enhanced filesystem
    fs_mgr = EnhancedAOSFSManager()
    
    # Start enhanced shell
    shell = EnhancedAlteronShell(fs_mgr)
    shell.start_shell()