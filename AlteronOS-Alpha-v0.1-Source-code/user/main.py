#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--no-login":
        from desktop import AlteronDesktop
        desktop = AlteronDesktop()
        desktop.run()
    else:
        from login import AlteronLogin
        login = AlteronLogin()
        login.run()

if __name__ == "__main__":
    main()