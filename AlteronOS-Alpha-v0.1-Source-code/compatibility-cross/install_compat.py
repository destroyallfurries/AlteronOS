#!/usr/bin/env python3
"""
AlteronOS Compatibility Dependency Installer - Python Version
Installs Wine, development tools, and emulation dependencies
"""

import os
import sys
import subprocess
import platform
import shutil
from pathlib import Path

class CompatibilityInstaller:
    def __init__(self):
        self.system = platform.system().lower()
        self.distro = self.detect_distro()
        self.install_log = []
        
    def detect_distro(self):
        """Detect Linux distribution"""
        if self.system != 'linux':
            return self.system
            
        try:
            with open('/etc/os-release', 'r') as f:
                for line in f:
                    if line.startswith('ID='):
                        return line.split('=')[1].strip().strip('"')
        except:
            pass
        return 'unknown'
        
    def run_command(self, cmd, sudo=False):
        """Run system command with error handling"""
        if sudo and os.geteuid() != 0:
            cmd = ['sudo'] + cmd
            
        print(f"🔧 Running: {' '.join(cmd)}")
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            self.install_log.append(f"✅ {cmd[0]}: Success")
            return True
        except subprocess.CalledProcessError as e:
            self.install_log.append(f"❌ {cmd[0]}: Failed - {e.stderr}")
            return False
        except FileNotFoundError:
            self.install_log.append(f"❌ {cmd[0]}: Command not found")
            return False
            
    def check_dependency(self, dep):
        """Check if dependency is installed"""
        return shutil.which(dep) is not None
        
    def install_windows_compatibility(self):
        """Install Wine and Windows compatibility tools"""
        print("\n" + "="*50)
        print("🪟 Installing Windows Compatibility (Wine)")
        print("="*50)
        
        if self.distro in ['ubuntu', 'debian']:
            commands = [
                ['dpkg', '--add-architecture', 'i386'],
                ['apt', 'update'],
                ['apt', 'install', '-y', 'wine', 'wine32', 'wine64', 'libwine', 'fonts-wine'],
                ['apt', 'install', '-y', 'winetricks']
            ]
        elif self.distro in ['arch', 'manjaro']:
            commands = [
                ['pacman', '-Sy', '--noconfirm', 'wine', 'winetricks']
            ]
        elif self.distro in ['fedora', 'centos', 'rhel']:
            commands = [
                ['dnf', 'install', '-y', 'wine', 'winetricks']
            ]
        else:
            print(f"❌ Unsupported distribution: {self.distro}")
            return False
            
        success = True
        for cmd in commands:
            if not self.run_command(cmd, sudo=True):
                success = False
                
        if success:
            # Verify Wine installation
            if self.check_dependency('wine'):
                version_result = subprocess.run(['wine', '--version'], capture_output=True, text=True)
                print(f"✅ Wine installed: {version_result.stdout.strip()}")
            else:
                print("❌ Wine installation verification failed")
                success = False
                
        return success
        
    def install_linux_development_tools(self):
        """Install Linux development and analysis tools"""
        print("\n" + "="*50)
        print("🐧 Installing Linux Development Tools")
        print("="*50)
        
        if self.distro in ['ubuntu', 'debian']:
            packages = [
                'python3-pip', 'python3-venv', 'nodejs', 'npm',
                'default-jre', 'openjdk-17-jre', 'binutils', 'file',
                'libc6-dev', 'build-essential', 'pkg-config'
            ]
            cmd = ['apt', 'install', '-y'] + packages
        elif self.distro in ['arch', 'manjaro']:
            packages = [
                'python-pip', 'nodejs', 'npm', 'jre-openjdk',
                'binutils', 'file', 'glibc', 'base-devel', 'pkgconfig'
            ]
            cmd = ['pacman', '-Sy', '--noconfirm'] + packages
        elif self.distro in ['fedora', 'centos', 'rhel']:
            packages = [
                'python3-pip', 'nodejs', 'npm', 'java-latest-openjdk',
                'binutils', 'file', 'glibc-devel', '@development-tools', 'pkgconfig'
            ]
            cmd = ['dnf', 'install', '-y'] + packages
        else:
            print(f"❌ Unsupported distribution: {self.distro}")
            return False
            
        success = self.run_command(cmd, sudo=True)
        
        # Verify installations
        tools = ['python3', 'node', 'java', 'file']
        for tool in tools:
            if self.check_dependency(tool):
                print(f"✅ {tool}: Installed")
            else:
                print(f"❌ {tool}: Not found")
                success = False
                
        return success
        
    def install_macos_compatibility(self):
        """Install macOS compatibility tools (Darling)"""
        print("\n" + "="*50)
        print "🍎 Installing macOS Compatibility (Darling)"
        print("="*50)
        
        # Note: Darling often needs to be built from source
        print("📝 Darling macOS compatibility layer installation:")
        print("  For most distributions, Darling needs to be built from source")
        print("  Visit: https://github.com/darlinghq/darling")
        print("  Or use your package manager if available")
        
        if self.distro in ['ubuntu', 'debian']:
            # Try to install from available repos
            if self.run_command(['apt', 'install', '-y', 'darling', 'darling-dkms'], sudo=True):
                print("✅ Darling installed from repository")
                return True
            else:
                print("ℹ️  Darling not in repositories, building from source required")
        elif self.distro in ['arch', 'manjaro']:
            if self.run_command(['pacman', '-Sy', '--noconfirm', 'darling', 'darling-dkms'], sudo=True):
                print("✅ Darling installed from AUR")
                return True
            else:
                print("ℹ️  Darling not in AUR, building from source required")
                
        print("💡 To install Darling manually:")
        print("  git clone https://github.com/darlinghq/darling.git")
        print("  cd darling && mkdir build && cd build")
        print("  cmake .. && make && sudo make install")
        
        return False  # Not installed by this script
        
    def install_cross_platform_tools(self):
        """Install cross-platform runtime tools"""
        print("\n" + "="*50)
        print("🌐 Installing Cross-Platform Runtimes")
        print("="*50)
        
        # Install Python packages
        python_packages = [
            'psutil', 'requests', 'pillow', 'numpy'
        ]
        
        print("📦 Installing Python packages...")
        for package in python_packages:
            try:
                subprocess.run([sys.executable, '-m', 'pip', 'install', package], 
                             capture_output=True, check=True)
                print(f"✅ Python: {package}")
            except subprocess.CalledProcessError:
                print(f"❌ Python: Failed to install {package}")
                
        # Install Node.js packages
        node_packages = [
            'express', 'axios', 'fs-extra'
        ]
        
        if self.check_dependency('npm'):
            print("📦 Installing Node.js packages...")
            for package in node_packages:
                try:
                    subprocess.run(['npm', 'install', '-g', package], 
                                 capture_output=True, check=True)
                    print(f"✅ Node.js: {package}")
                except subprocess.CalledProcessError:
                    print(f"❌ Node.js: Failed to install {package}")
                    
        return True
        
    def setup_alteronos_environment(self):
        """Setup AlteronOS specific environment"""
        print("\n" + "="*50)
        print("⚙️ Setting up AlteronOS Environment")
        print("="*50)
        
        # Create AlteronOS directories
        directories = [
            'A:/Alteron/System',
            'A:/Alteron/Programs', 
            'A:/Alteron/Users',
            'A:/Alteron/Config',
            'A:/Alteron/Temp',
            '~/.alteronos',
            '~/.alteronos/cache',
            '~/.alteronos/config'
        ]
        
        for directory in directories:
            dir_path = Path(directory.replace('A:/', '/opt/alteronos/'))
            try:
                dir_path.mkdir(parents=True, exist_ok=True)
                print(f"✅ Created: {dir_path}")
            except Exception as e:
                print(f"❌ Failed to create {dir_path}: {e}")
                
        # Create Wine prefix for AlteronOS
        wine_prefix = Path.home() / '.alteronos' / 'wine'
        os.environ['WINEPREFIX'] = str(wine_prefix)
        
        if not wine_prefix.exists():
            print("🍷 Setting up Wine prefix for AlteronOS...")
            if self.run_command(['wine', 'wineboot', '--init']):
                print("✅ Wine prefix created")
            else:
                print("❌ Failed to create Wine prefix")
                
        return True
        
    def verify_installations(self):
        """Verify all installations"""
        print("\n" + "="*50)
        print("🔍 Verifying Installations")
        print("="*50)
        
        checks = [
            ('Wine', 'wine'),
            ('Python 3', 'python3'),
            ('Node.js', 'node'),
            ('Java', 'java'),
            ('File utility', 'file'),
            ('Binutils', 'objdump')
        ]
        
        all_ok = True
        for name, command in checks:
            if self.check_dependency(command):
                # Get version if possible
                try:
                    result = subprocess.run([command, '--version'], capture_output=True, text=True)
                    version = result.stdout.split('\n')[0] if result.stdout else 'Installed'
                    print(f"✅ {name}: {version}")
                except:
                    print(f"✅ {name}: Installed")
            else:
                print(f"❌ {name}: Not installed")
                all_ok = False
                
        return all_ok
        
    def install_all(self):
        """Install all compatibility components"""
        print("🚀 AlteronOS Compatibility Dependency Installer")
        print("="*60)
        print(f"System: {self.system}, Distribution: {self.distro}")
        print("="*60)
        
        # Check if we have sudo privileges
        if os.geteuid() != 0:
            print("🔒 This installer may require sudo privileges for package installation")
            print("   Please enter your password when prompted")
        
        installations = [
            ("Windows Compatibility", self.install_windows_compatibility),
            ("Linux Development Tools", self.install_linux_development_tools),
            ("macOS Compatibility", self.install_macos_compatibility),
            ("Cross-Platform Tools", self.install_cross_platform_tools),
            ("AlteronOS Environment", self.setup_alteronos_environment)
        ]
        
        results = {}
        for name, installer in installations:
            print(f"\n🎯 {name}")
            print("-" * 30)
            results[name] = installer()
            
        # Final verification
        print("\n" + "="*60)
        print("📊 Installation Summary")
        print("="*60)
        
        all_success = True
        for name, success in results.items():
            status = "✅ Success" if success else "❌ Failed"
            print(f"{status}: {name}")
            if not success:
                all_success = False
                
        # Final verification check
        final_ok = self.verify_installations()
        
        print("\n" + "="*60)
        if all_success and final_ok:
            print("🎉 All compatibility components installed successfully!")
            print("\nAlteronOS can now run:")
            print("  🪟 Windows applications (.exe, .msi) via Wine")
            print("  🐧 Linux applications (.deb, ELF binaries) natively")
            print("  🍎 macOS applications (.app, .dmg) via Darling")
            print("  🌐 Cross-platform apps (.py, .js, .jar)")
        else:
            print("⚠️ Some components failed to install")
            print("Check the log above and install missing dependencies manually")
            
        return all_success and final_ok

def main():
    """Main installation function"""
    if len(sys.argv) > 1 and sys.argv[1] == '--check-only':
        # Just check existing dependencies
        installer = CompatibilityInstaller()
        installer.verify_installations()
        return
        
    installer = CompatibilityInstaller()
    
    # Confirm installation
    print("This will install compatibility dependencies for AlteronOS:")
    print("  - Wine (Windows application support)")
    print("  - Development tools (Python, Node.js, Java)")
    print("  - System utilities (binutils, file)")
    print("  - Cross-platform runtimes")
    print("\nThis may require sudo privileges and internet access.")
    
    response = input("\nContinue? (y/N): ").lower().strip()
    if response not in ['y', 'yes']:
        print("Installation cancelled.")
        return
        
    success = installer.install_all()
    
    if success:
        print("\n🎊 AlteronOS compatibility layer is ready!")
        print("You can now run applications from Windows, Linux, and macOS!")
    else:
        print("\n💡 Some installations failed. You may need to:")
        print("  1. Check your internet connection")
        print("  2. Install missing dependencies manually")
        print("  3. Run this script again")
        sys.exit(1)

if __name__ == "__main__":
    main()