#!/usr/bin/env python3
import shutil
import sys

deps = [
    ('python', 'python'),
    ('gcc', 'gcc'),
    ('rust', 'rustc'),
    ('go', 'go'),
    ('nasm', 'nasm'),
    ('qemu', 'qemu-system-x86_64')
]

print("Checking dependencies...")
for name, cmd in deps:
    if shutil.which(cmd):
        print(f"✅ {name}")
    else:
        print(f"❌ {name}")

print("\nAlteronOS build system ready!")